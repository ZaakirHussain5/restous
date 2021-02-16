from django.shortcuts import render,redirect
from django.contrib.auth import login,get_user_model,logout
from api.restraunt.models import restraunt

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            if user.check_password(password):
                login(request,user)
                return redirect('/Home')
        except UserModel.DoesNotExist:
            return redirect('/')

    return render(request,'resto/login.html')

def Restraunts(request):
    return render(request,'resto/restraunts.html')

def Managers(request):
    restraunts = restraunt.objects.all()
    return render(request,'resto/managers.html',{
        "restraunts": restraunts
    })

def Transactions(request):
    return render(request,'resto/transactions.html')

def Home(request):
    return render(request,'resto/home.html')
def Users(request):
    return render(request,'resto/users.html')

def signOut(request):
    logout(request)
    return redirect('/')