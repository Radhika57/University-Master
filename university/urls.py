"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from app import API_Views
# from university import views
from app.views import * 
from app import views
from django.conf.urls import handler404

admin.site.site_header = 'My project'
admin.site.site_title = "Welcom to Admin Panel"
admin.site.index_title="Welcome to this Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/result', API_Views.StudentList.as_view()),
    path("",LoginView.as_view(),name="login"),
    # path("dashboard/",views.dashboard,name="dashboard"),
    # path('dashboard/', StudentCreateView.as_view(), name='dashboard'),
    path('studentdata/',StudentListView.as_view(),name='studentdata'),
    path('university',UniversityCreateView.as_view(),name='university'),
    path('delete/<int:pk>', DeleteView.as_view(),name='delete'),
    path('dashboard/',views.dashboard,name="dashboard")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
handler404 = views.error_404
