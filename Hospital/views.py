from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
# from django.db import models
# models.get_models(include_auto_created=True)
from django.contrib import messages, auth

from . decorators import *

def home1(request):
    return render(request, 'Hospital/index3.html')

def medcategory(request):
    return render(request, 'Hospital/medcategory.html')

def medinvent(request):
    return render(request, 'Hospital/medinvent.html')

def sales(request):
    return render(request, 'Hospital/sales.html')

def staff(request):
    return render(request, 'Hospital/staff.html')

def expense(request):
    return render(request, 'Hospital/expense.html')

def expensecategory(request):
    return render(request, 'Hospital/expensecategory.html')


