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


    context = {"user":name,"authenticate":user_auth,"posts":post_form}


    return render(request,"main/home.html",context)


@login_required
def post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            # delay the save method 
            post = form.save(commit=False)
            # assgin the post name to the user 
            post.name = request.user
            # save the post
            post.save()
           
        return redirect("home")
    

    else:
        # give the chance to visit the post page and post something if needed 
        form = PostForm()
        # show the user his own name 
        name = request.user.username
        user_auth = request.user.is_authenticated
        context = {"form":form,"user":name,"authenticate":user_auth}

    return render(request,"main/posts.html",context)
    

@login_required
def comment_view(request,id):

    user_auth = request.user.is_authenticated
    if request.method == "POST":
        # get the comment message fro the form
        comment = request.POST['comment']
        if comment:
             # get the user who commented the message
            username =  request.user
            # get the post where the comment meesage sent to 
            post = Post.objects.get(id=id)
            # store the comment message, user, and the commented post 
            comments = Comment(name=username,comment=comment,post=post)
            comments.save()
            # get the related cooments to this post 
            get_comments = Comment.objects.filter(post=post)
            # clean the data and get the post with its user
            for item in get_comments :
                item = item
                get_user = item.name

            # show the delete button and give the user the chance to delete his own comments 
            if username == get_user:
                delete_comment = True

            context = {"comments":get_comments,"item":item,"delete_comment":delete_comment,"authenticate":user_auth}
           
        return render(request,"main/comment.html",context)    

    else:
        # get the user post 
        post = Post.objects.get(id=id)
        get_comments = Comment.objects.filter(post=post)
        # get all of the posts related to that user 
        related_posts = Post.objects.filter(name=post.name).exclude(id=id)
        print(related_posts)
        for item in get_comments :
                item = item
                get_user = item.name

        if request.user == get_user:
            delete_comment = True
    
        context = {"comments":get_comments,"item":item,"delete_comment":delete_comment,
                   "authenticate":user_auth,"posts":related_posts}

        return render(request,"main/comment.html",context)
    

# delete commente 
def delete_comments(request,id):
    if request.method == "POST":
        # get the comment 
        comment = Comment.objects.get(id=id)
        # prevent the user from deleting other users' comments
        if request.user == comment.name:
            comment.delete()

        return redirect("home")


    
