from django.shortcuts import render , HttpResponse

# Create your views here.
def home(index):
    return HttpResponse("this is home ")
def contact(index):
    return HttpResponse("this is contact ")
def about(index):
    return HttpResponse("this is about page ")