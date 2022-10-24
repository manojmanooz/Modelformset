from django.shortcuts import render,HttpResponse
from .models import Crud
from django.forms import modelformset_factory
from django import forms
from .forms import crudform
# Create your views here.

def home(request):
    obj=modelformset_factory(Crud,crudform)

    if request.method == 'GET':
        form=obj(request.GET)
        form.save()
        print(form)
    form=obj()
    return render(request,'index.html',{'form':form})