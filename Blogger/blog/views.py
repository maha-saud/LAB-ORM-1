from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Post
from .forms import PostForm


def create_blog_view(request:HttpRequest):

    post_form = PostForm()

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('main:home_view')
        else:
            print("not valid form")

    return render(request, "blog/create.html", {"post_form":post_form})


def blog_detail_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    return render(request, 'blog/blog_detail.html', {"post" : post})


def blog_update_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = request.POST.get("is_published") == "on"
        if "poster" in request.FILES: post.poster = request.FILES["poster"]
        post.save()

        return redirect("blog:blog_detail_view", post_id=post.id)

    return render(request, "blog/blog_update.html", {"post":post})


def blog_delete_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect("main:home_view")


def all_posts_view(request:HttpRequest):

    posts = Post.objects.all().order_by("-published_at")

    print(posts.count())

    return render(request, "blog/all_posts.html", {"posts":posts})


def search_posts_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 3:
        posts = Post.objects.filter(title__contains=request.GET["search"])

        if "order_by" in request.GET and request.GET["order_by"] == "published_at":
            posts = posts.order_by("-published_at")
    else:
        posts = []

    return render(request, "blog/search_posts.html", {"posts" : posts})
