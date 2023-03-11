from atexit import register
from dataclasses import fields
from rest_framework import serializers
from .models import *


class StudentSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"




# class LoginSerliazer(serializers.Serializer):
#     reg = serializers.CharField
#     class Meta:
#         fields=('reg')
    # email = serializers.EmailField
    # password = serializers.CharField
    # class Meta:
       
    #     fields = ('email','password')  
        
