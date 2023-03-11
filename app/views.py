from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from app.forms import *
from app.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard')
    
# class StudentCreateView(SuccessMessageMixin,CreateView):
#     form_class = StudentForm
#     model= Student
#     # data = University.objects.all()
#     template_name = 'dashboard.html'
#     success_url = reverse_lazy('dashboard')
#     success_message = 'Result Uploded Successfully !!!!'

@login_required
def dashboard(request):
    data = University.objects.all()
    if request.method=="POST":
        university_id = request.POST.get('university_id')
        university_name = University.objects.get(id=university_id)
        registration_no = request.POST.get('registration_no')
        student_result = request.FILES.get('result')
        data1 = Student(user=request.user,university_name=university_name,registration_no=registration_no,student_result=student_result)
        data1.save()
        messages.success(request, 'Result Uploaded Succesfully')
    return render(request,"dashboard.html",{'data':data})  
    

class StudentListView(LoginRequiredMixin,ListView):
    template_name = 'studentdata.html'
    # queryset = Student.objects.all()  
    model = Student
    context_object_name = 'students'  
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
            
        return queryset.filter(user__username=self.request.user.username)

class UniversityCreateView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,CreateView):
    form_class = UniversityForm
    model = University
    template_name = 'university.html'
    success_url = reverse_lazy('university')
    success_message = 'University Added Successfully !!!!'
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('dashboard') 
        else:
            return redirect('login')
 
class DeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    success_url ="/studentdata/"
    template_name = 'delete.html'
    
def error_404(request, exception):
   context = {}
   return render(request,'404.html', context)
    