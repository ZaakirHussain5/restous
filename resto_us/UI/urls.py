from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('login',views.signIn,name="SignIn"),
    path('Transactions',views.Transactions,name="Transactions"),
    path('Restraunts',views.Restraunts,name="Restraunts"),
    path('Managers',views.Managers,name="Managers"),
    path('Users',views.Users,name="Users"),
    path('signOut',views.signOut,name="UOMs"),
]