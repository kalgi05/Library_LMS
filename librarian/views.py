from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
import datetime
from .utils import embed_QR
import os
import base64
# from .forms import *
from .models import *
import random

def DashboardLib(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            enrollment = request.POST['enrollment']
            print(enrollment)
            stu = Student.objects.get(enrollment = enrollment)
            print('before',stu.present)
            
            if stu.present == True:
                msg = stu.enrollment+": Entry"
                stu.outtime = datetime.datetime.now()
                stu.present = False
                stu.save()
            else:
                msg = stu.enrollment+": Exit"
                stu.intime = datetime.datetime.now()
                stu.present = True
                stu.save()
            print('after',stu.present)
            return render(request, 'Lib/index.html', {'username': request.user, 'msg' : msg})
        else:
            # print(datetime.datetime.now())
            return render(request, 'Lib/index.html', {'username': request.user} )
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
            return redirect('/librarian')

            # return redirect('index')
        else:
            print('invalid password')
            return render(request, 'Lib/login.html')

        # form = AuthenticationForm()
        # return render(request, 'Lib/login.html', {'form':form, 'title':'log in'})
    else:
        return render(request, 'Lib/login.html')

def Logout(request):
    logout(request)
    return redirect('/librarian/login')


        
def BooksHome(request):
    if request.user.is_authenticated:
        books = Books.objects.all()
        # print(books)
        return render(request, 'Lib/books.html', {'username': request.user, 'books' : books} )
    else:
        return redirect('/librarian/login')
    
def AddBooks(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            bName = request.POST['name']
            bAuthor = request.POST['author']
            publisher = request.POST['publisher']
            edition = request.POST['edition']
            category = request.POST['category']
            price = request.POST['price']
            pubYear = request.POST['pubYear']
            totQuant = request.POST['totQuant']
            curAvail = request.POST['curAvail']

            book = Books(bName = bName,
                         author = bAuthor, 
                         publisher = publisher,
                         edition = edition, 
                         category = category,
                         Price = price, 
                         PubYear = pubYear, 
                         totAvail = curAvail, 
                         totQuant = totQuant)
            print(bName, bAuthor)
            print("book object ",book)
            bId = book.insertBook()
            url = bId
            bId += ".png"
            embed_QR(url, bId)
            with open(bId, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')

            return render(request, 'Lib/add-books.html', {'username': request.user, 'BQR': image_data} )
        else:
            
            return render(request, 'Lib/add-books.html', {'username': request.user} )
    else:
        
        return redirect('/librarian/login')

def EditBooks(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            upBook = Books.objects.get(bookId=request.GET.get('bId'))
            upBook.bName = request.POST['name']
            upBook.author = request.POST['author']
            upBook.publisher = request.POST['publisher']
            upBook.edition = request.POST['edition']
            upBook.category = request.POST['category']
            upBook.Price = request.POST['price']
            upBook.PubYear = request.POST['pubYear']
            upBook.totQuant = request.POST['totQuant']
            upBook.totAvail = request.POST['curAvail']
            upBook.save()
            
            

            return render(request, 'Lib/edit-books.html', {'username': request.user, 'bookData': upBook} )
        else:
            # print("value", request.GET.get('bId'))
            upBook = Books.objects.get(bookId=request.GET.get('bId'))
            # print(upBook.bName)
            return render(request, 'Lib/edit-books.html', {'username': request.user, 'bookData': upBook} )
    else:
        return redirect('/librarian/login')
    
def DeleteBooks(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            return render(request, 'Lib/edit-books.html', {'username': request.user} )
        else:
            print("value", request.GET.get('bId'))
            upBook = Books.objects.get(bookId=request.GET.get('bId'))
            print(upBook.bName)
            upBook.delete()
            books = Books.objects.all()
            return redirect('/librarian/books')
            # return render(request, 'Lib/books.html', {'username': request.user, 'books' : books} )
    else:
        return redirect('/librarian/login')
    
def LibStudent(request):
    if request.user.is_authenticated:
        Students = Student.objects.all()
        # print(Students)
        
        return render(request, 'Lib/students.html', {'username': request.user, 'students': Students} )
    else:
        return redirect('/librarian/login')

def EditStudent(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            upStu = Student.objects.get(enrollment=request.GET.get('stuId'))
            upStu.panenlty = request.POST['panelty']
            print(request.POST.get('approved'))
            if request.POST.get('approved') == "on":
                upStu.approved = True
                print("true")
            else:
                upStu.approved = False
                print("false")
            
            upStu.save()
            return render(request, 'Lib/edit-students.html', {'username': request.user, 'stuData': upStu} )
        else:
            # print("value", request.GET.get('stuId'))
            upStu = Student.objects.get(enrollment=request.GET.get('stuId'))
            # print(upStu.enrollment)
            return render(request, 'Lib/edit-students.html', {'username': request.user, 'stuData': upStu} )
    else:
        return redirect('/librarian/login')