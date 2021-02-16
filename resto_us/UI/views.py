from django.shortcuts import render,redirect
from django.contrib.auth import login,get_user_model,logout
from api.restraunt.models import restraunt
from django.contrib.auth.decorators import login_required
from api.transactions.models import transaction
from api.restraunt.models import restraunt
from api.user.models import resto_user


def signIn(request):
    return render(request,'resto/login.html')

@login_required(login_url='/login')
def Restraunts(request):
    return render(request,'resto/restraunts.html')

@login_required(login_url='/login')
def Managers(request):
    restraunts = restraunt.objects.all()
    return render(request,'resto/managers.html',{
        "restraunts": restraunts
    })

@login_required(login_url='/login')
def Transactions(request):
    return render(request,'resto/transactions.html')

@login_required(login_url='/login')
def Home(request):
    return render(request,'resto/home.html',{
        "transCount":len(transaction.objects.all()),
        "usersCount":len(resto_user.objects.filter(user_type="U")),
        "restrauntsCount":len(restraunt.objects.all())
    })

@login_required(login_url='/login')
def Users(request):
    return render(request,'resto/users.html')

@login_required(login_url='/login')
def signOut(request):
    logout(request)
    return redirect('/')