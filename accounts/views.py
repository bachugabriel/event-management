from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def user_register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirmpassword=request.POST.get('pass2')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
            else:
                user_register=User.objects.create_user(username=username,email=email,password=password)
                user_register.save()
                messages.info(request, 'User Successfully created')
                return redirect('/accounts/user_login')
        else:
            messages.info(request, "Password doesn't match")
            return redirect('/accounts')
    return render(request, 'user/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials !")
            return redirect('/accounts')
    return render(request, 'user/login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('/')