from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from blog.models import Post

def home_view(request:HttpRequest):
    #get all posts
    posts = Post.objects.all()
    return render(request, "main/home.html", {"posts": posts})


def mode_view(request: HttpRequest, mode: str):
    response = redirect(request.GET.get("next", "/"))
    if mode in ["light", "dark"]:
        response.set_cookie("mode", mode, max_age=60*60*24*365)
    return response

'''
def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response
'''