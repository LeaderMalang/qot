from django.shortcuts import render, redirect
from .models import Services, Contact, Package
# Create your views here.

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['fullName']
        mobile = request.POST['mobile']
        email = request.POST['email']
        country = request.POST['country']
        message = request.POST['message']
        contact = Contact(full_name=full_name, mobile=mobile, email=email, country=country, message=message)
        contact.save()
        return redirect('/contact/')
    return render(request, 'contact.html')

def courses(request):
    courses = Services.objects.all()
    return render(request, 'courses.html', {'courses':courses})

def packages(request):
    packages = Package.objects.all()
    return render(request, 'packages.html', {'packages':packages})