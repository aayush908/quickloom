from django.shortcuts import render , HttpResponse
from blog.models import Post

# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    context = {'allpost' : allpost}
    return render(request ,'blog/blog.html' , context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)

