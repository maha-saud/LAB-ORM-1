from django.shortcuts import render
from blog.models import Post

def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by("-published_at")
    context = {"posts": posts}
    return render(request, "main/home.html", context)
