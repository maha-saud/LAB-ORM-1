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

    def __str__(self):
        # عشان يظهر العنوان في لوحة التحكم
        return self.title
