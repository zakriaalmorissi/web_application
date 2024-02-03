from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Comment
from django.contrib.auth.models import User


# Create your views here.

# home pages view
def home_view(request):
    name = request.user.username
    name = name.title()
    user_auth = request.user.is_authenticated
    # posts forms 
    post_form = Post.objects.all()


    # comments 
    comment = Comment.objects.all()
    print(Post.message)

    context = {"user":name,"authenticate":user_auth,"posts":post_form,"comments":comment}


    return render(request,"main/home.html",context)


@login_required
def comment_view(request,id):
    if request.method == "POST":
        comment = request.POST['comment']
        if comment:
            username =  request.user
            post = Post.objects.get(id=id)
            comments = Comment(name=username,comment=comment,post=post)
            comments.save()

            get_comments = Comment.objects.filter(post=post)
            for item in get_comments :
                item = item

           
        return render(request,"main/comment.html",{"comments":get_comments,"item":item})


    return redirect("home")




@login_required
def post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            print(post.name)
            post.save()
           
        return redirect("home")
    

    else:
        form = PostForm()
        name = request.user.username
        user_auth = request.user.is_authenticated
        context = {"form":form,"user":name,"authenticate":user_auth}

    return render(request,"main/posts.html",context)
    
    
