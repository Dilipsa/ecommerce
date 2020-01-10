from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Home

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(first_name)
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1,  email = email, first_name = first_name, last_name = last_name)
                user.save();
                print("success")
                return redirect('/accounts/otp/')
        else:
            print("password not matching")
            return redirect('register')
        return redirect('/')

    else:
        data = Home.objects.all()
        return render(request,'register.html',{'data':data})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def otp(request):
    if request.method == "POST":
        otp = request.POST['otp']
        if otp=='123':
            return redirect('thanku')
    return render(request, 'otp.html')

def thanku(request):
    return render(request, 'thanku.html')


def cart(request):
    data = Home.objects.all()
    return render(request,'cart.html', {'data':data})
