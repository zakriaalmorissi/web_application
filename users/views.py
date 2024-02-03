from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        # get the user inputs 
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect("home")
        else:
            error_message = "invalid username or password !"
            return render(request,"login.html",{"form":form,"error_message":error_message})

    else:
        form = LoginForm()  
            
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

def sign_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():    
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password) 
            login(request,user)
            return redirect('home')

    form = SignupForm()
    return render(request, "sign.html", {"forms": form})
