from django.shortcuts import render , HttpResponse

# Create your views here.
def home(index):
    return HttpResponse("this is home ")
def bg(index):
    return HttpResponse("yes how may help you ")
