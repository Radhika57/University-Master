from rest_framework.viewsets import ViewSet,ModelViewSet
from app import serialziers
from app.serialziers import StudentSerliazer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics



class StudentList(generics.ListAPIView):
    serializer_class =StudentSerliazer
    def get_queryset(self):
        reg = self.request.GET.get('reg')
        
        
        student = Student.objects.filter(registration_no=reg)

       
        return student
    

   




# class loginList(APIView):
#     queryset = Student.objects.all()     
#     serializer_class  = LoginSerliazer
# class loginList(APIView):
#     serializer_class = LoginSerliazer
#     def post(self,request,*args, **kwargs):
#         email = request.POST.get('reg')
#         print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",email)
    # # def get(self,request):
    # #     Reg = request.GET.get("reg")
    # #     stu =Student.objects.filter(registration_no=Reg)
    # #     # student = Student.objects.all()
    # #     # serializer = LoginSerliazer(student,many=True)
    # #     return Response(stu)

    # def post(self):
    #     pass