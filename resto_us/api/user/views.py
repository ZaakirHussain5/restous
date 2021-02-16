from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import resto_user_serailazer,usersListSerializer
from .models import resto_user
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout

import re
import random

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signIn(request):
    if not request.method == 'POST':
        return JsonResponse({"error","Send a Post Request with valid parameters"})
    
    username = request.POST['email']
    password = request.POST['password']
    
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({"error":"Previous Session Exists"})
            
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request,user)
            return JsonResponse({"token":token,"user":usr_dict})
        else:
            return JsonResponse({"error":"Authentication Failed Check your username and Password"})
    except UserModel.DoesNotExist:
        return JsonResponse({"error":"Authentication Failed Check your username and Password"})

def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({"error":"Invalid User ID"})

    return JsonResponse({"message":"Logout Success!!"})

class userViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {"create" : {AllowAny}}

    serializer_class = resto_user_serailazer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
    
    def get_queryset(self):
        queryset = resto_user.objects.all().order_by('id')
        email = self.request.query_params.get('email',None)
        phone = self.request.query_params.get('phone',None)
        userType = self.request.query_params.get('userType',None)
        self.serializer_class = usersListSerializer
        if userType is not None :
            queryset = resto_user.objects.filter(user_type=userType)
        if email is not None:
            queryset = resto_user.objects.filter(email=email)
        if phone is not None:
            queryset = resto_user.objects.filter(phone=phone)
        return queryset


