from django.shortcuts import render , HttpResponse , redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras
from django.contrib.auth.models import User


# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    context = {'allpost' : allpost}
    return render(request ,'blog/blog.html' , context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
        
    return redirect(f"/blog/{post.slug}")

def writeblog(request):
    if request.method=="POST":
        author=request.POST['author']
        title=request.POST['title']
        slug=request.POST['slug']
        content =request.POST['content']
        if len(author)<2 or len(title)<3 or len(slug)<3 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            blog = Post(title=title, author=author, slug=slug, content=content)
            blog.save()
            messages.success(request, "Your  blog has been successfully sent")
    return render(request, "blog/writeblog.html")

