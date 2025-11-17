from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("create/", views.create_blog_view, name="create_blog_view"),
    path("detail/<post_id>/", views.blog_detail_view, name="blog_detail_view"),
    path("update/<post_id>/", views.blog_update_view, name="blog_update_view"),
    path("delete/<post_id>/", views.blog_delete_view, name="blog_delete_view"),
    path("all/", views.all_posts_view, name="all_posts_view"),
    path("search/", views.search_posts_view, name="search_posts_view"),
]
