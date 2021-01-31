from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('user/',include('api.user.urls')),
    path('transactions/',include('api.transactions.urls')),
    path('restraunts/',include('api.restraunt.urls')),
]
