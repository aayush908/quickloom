from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post


# Create your views here.
def home(request):
    allpost = Post.objects.all()
    context = {'allpost' : allpost}
    return render(request, "home/home.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
             messages.error(request ,"please fill the form correctly")
        else:
             
            contact2 = Contact(name=name, email=email, phone=phone, content=content)
            contact2.save()
            messages.success(request ," Your form succesfully  received ")

   
    return render(request, "home/contact.html" )


def about(request):
    return render(request, "home/about.html")

def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
    
    params={'allPosts': allPosts}
    return render(request, 'home/search.html', params)
