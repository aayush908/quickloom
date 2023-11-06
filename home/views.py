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
    if len(query) >78:
        allPosts = Post.objects.none()
    else:
        allPoststitle= Post.objects.filter(title__icontains=query)
        allPostsauthor= Post.objects.filter(author__icontains=query)
        allPostscontent= Post.objects.filter(content__icontains=query)
        allPosts = allPoststitle.union(allPostscontent , allPostsauthor)
    if allPosts.count() == 0:
        messages.warning(request , "no search result found")
    params={'allPosts': allPosts , 'query' :query}
    return render(request, 'home/search.html', params )
