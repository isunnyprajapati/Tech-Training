from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact

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