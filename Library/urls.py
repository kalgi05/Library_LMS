"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardLib, name='Library'),
    path('login', views.Login, name='Login'),
    path('logout', views.Logout, name='logout'),
    # path('students', views.LibStudent, name='Students Librarian'),
    # path('students/editStudent', views.EditStudent, name='Edit Student'),
    path('books', views.BooksHome, name='Books'),
    path('books/issueBook', views.IssueBook, name='Issue Books'),
    # path('books/addBooks', views.AddBooks, name='Add Books'),
    # path('books/editBook', views.EditBooks, name='Edit Books'),
    # path('books/deleteBook', views.DeleteBooks, name='Delete Books'),
    
    # path('register', views.Register, name='Register'),
    # path('registered', views.Generate, name='QRRegister')
]
