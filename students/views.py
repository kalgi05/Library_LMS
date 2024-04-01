from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .utils import embed_QR
import os
import base64
from .forms import *
from .models import *
from .forms import RegisterForm


# Create your views here.

def Dashboard(request):
    return render(request, 'index.html')

'''def Books(request):
    if 'student' in request.session:
        return render(request, 'books.html')
    else:
        return redirect('/login') 
'''
def communication(request):
        return render(request, 'communication.html')

def poetry(request):
        return render(request, 'poetry.html')

def inspiration(request):
        return render(request, 'inspiration.html')

def Books(request):
        return render(request, 'books.html')

def Contact(request):
    return render(request, 'contact.html')

def product_details(request):
    return render(request, 'product-details.html')

def details1(request):
      return render(request, 'details1.html')

def details2(request):
      return render(request, 'details2.html')

def details3(request):
      return render(request, 'details3.html')

def details4(request):
      return render(request, 'details4.html')

def details5(request):
      return render(request, 'details5.html')

def details6(request):
      return render(request, 'details6.html')

def details7(request):
      return render(request, 'details7.html')
      

# @csrf_exempt
def Register(request):
    reg = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = url = form.cleaned_data['enrollment']
            form.save()
            name += ".png"
            embed_QR(url, name)
            with open(name, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
            #return render(request, 'register.html', {'registerForm' : reg, 'QR': image_data, 'details': url })
        else:
            print('Not working')
       # url = print(request.POST['enrollment'])
        
        return render(request, 'register.html', {'registerForm' : reg, 'QR': image_data, 'details': url })
    else:
        return render(request, 'register.html', {'registerForm' : reg})

def Login(request):
    if request.method == 'POST':
        enrollment = request.POST['enrollment']
        email = request.POST['email']
        password = request.POST['password']
        print(enrollment, email, password)
        stu = Student.get_student_by_enrollment(enrollment)
        print("stu object", stu)
        if stu:
            if stu.password == password:
                # print('success')
                request.session['student'] = enrollment
                print("session value", request.session['student'])
                return  redirect('/') 
            else:
                print('invalid password')
                return render(request, 'login.html')
        else:
            print('user does not exits')
            return render(request, 'login.html')
   
    else:
        return render(request, 'login.html')
            
def Logout(request):
    del request.session['student']
    return  redirect('/') 
    # return render(request, 'login.html')
