from django.db import models
from django.utils import timezone

class Post(models.Model):
    # عنوان التدوينة
    title = models.CharField(max_length=2048)

    # نص التدوينة
    content = models.TextField()

    # هل التدوينة منشورة ولا مخفية
    is_published = models.BooleanField(default=True)

    # وقت النشر (الافتراضي الآن)
    published_at = models.DateTimeField(default=timezone.now)
    # حقل اضافي لستقبال الصور من اليوزر 
    poster = models.ImageField(upload_to="images/", default="images/default.jpg") # كتنظيم ولا يمديني استغني عنها و بس اكتب ابلود تو مباشرة 
    # عينت قيمه افتراضيه لو ما حط اليوزر صوره هي تتعين تلقائي او لو اضفتها بعدين الي ما كان لهم صور تصير هذي الصوره لهم تتعين 
