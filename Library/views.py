from django.shortcuts import render
from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
import datetime
import os
import base64
from librarian.models import *
from students.models import *
# from .forms import *
import random

# Create your views here.

def DashboardLib(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # enrollment = request.POST['enrollment']
            # print(enrollment)
            # stu = Student.objects.get(enrollment = enrollment)
            # print('before',stu.present)
            
            # if stu.present == True:
            #     msg = stu.enrollment+": Entry"
            #     stu.outtime = datetime.datetime.now()
            #     stu.present = False
            #     stu.save()
            # else:
            #     msg = stu.enrollment+": Exit"
            #     stu.intime = datetime.datetime.now()
            #     stu.present = True
            #     stu.save()
            # print('after',stu.present)
            return render(request, 'Library/index.html', {'username': request.user, 'msg' : msg})
        else:
            # print(datetime.datetime.now())
            return render(request, 'Library/index.html', {'username': request.user} )
    else:
        return redirect('/librarian/login')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username = username, password = password)
        print('print user', user)
        if user is not None:
            form = login(request, user)
            print('print form', form)
            print('login success')
            return redirect('/Library')

            # return redirect('index')
        else:
            print('invalid password')
            return render(request, 'Library/login.html')

        # form = AuthenticationForm()
        # return render(request, 'Lib/login.html', {'form':form, 'title':'log in'})
    else:
        return render(request, 'Library/login.html')

def BooksHome(request):
    if request.user.is_authenticated:
        books = Books.objects.all()
        # print(books)
        return render(request, 'Library/books.html', {'username': request.user, 'books' : books} )
    else:
        return redirect('/librarian/login')
    
def IssueBook(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get('bId'):
                isubooks = Books.objects.get(bookId=request.POST.get('bId'))
            
            if request.POST.get('stuId'):
                stuId = Student.objects.get(enrollment=request.POST.get('stuId'))
    
            print(isubooks)
            
            return render(request, 'Library/issue-books.html', {'username': request.user, 'bookData': isubooks} )
    
        else:
            # print("value", request.GET.get('bId'))
            # isuBook = Books.objects.get(bookId=request.GET.get('bId'))
            # # print(upBook.bName)
            return render(request, 'Library/issue-books.html', {'username': request.user, } )
    else:
        return redirect('/Library/login')


       


def Logout(request):
    logout(request)
    return redirect('/Library/login')

