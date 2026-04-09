from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.


def index(request):
    # return HttpResponse("hello")
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name, 
            phone=phone, 
            email=email, 
            message=message
        )
        return redirect('contacts')
    data = Contact.objects.all()
    return render(request, 'contacts.html', {'data': data})

def catalog(request):
    return render(request, 'catalog.html')

def signup(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create_user(
            username = username, 
            email = email, 
            password = password
        )
        user.save()
        return redirect('index')
    return render(request, 'signup.html')

def login(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('username')
        
        user = authenticate(request, username=username, password=password)
        
    return render(request, 'login.html')
