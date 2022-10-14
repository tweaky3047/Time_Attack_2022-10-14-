from django.shortcuts import render,redirect
from .models import UserModel
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        phone_number = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')
        UserModel.objects.create_user(username=username, password=password, phone_number=phone_number, address=address)
        return redirect('/login')
       
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        me = auth.authenticate(request, username= username, password = password)

        if me is not None:
            auth.login(request, me)
            request.session['user']= me.username
            return redirect('/home')
        else:
            return render(request,'login.html',)
            
    elif request.method == 'GET':
        if request.method == 'GET':
            user = request.user.is_authenticated
            if user:
                return redirect('/home')
            else:
                return render(request, 'login.html')

def home(request):       
    user = request.user.is_authenticated
    if user:
        return render(request,'home.html/')
    else:
        return  redirect('/login')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login')