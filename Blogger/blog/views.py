from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post


def create_blog_view(request):
    # لو الفورم انرسل
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        is_published = request.POST.get("is_published") == "on"

        # تأكد بسيط إن فيه عنوان ومحتوى
        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                is_published=is_published,
                published_at=timezone.now()
            )
            # رجوع للصفحة الرئيسية بعد الحفظ
            return redirect("main:home_view")

    # لو GET أو فورم ناقص، أعرض صفحة الإضافة
    return render(request, "blog/create.html")
