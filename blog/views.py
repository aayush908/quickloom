from django.shortcuts import render , HttpResponse

# Create your views here.
def bloghome(request):
    return  render(request , 'blog/blog.html')
def blogpost(index , slug):
    return HttpResponse(f"this is blogpost :  {slug} ")

