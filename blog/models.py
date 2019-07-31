from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField

STATUS = (
    (0, "Taslak"),
    (1, "Yayına Hazır"),
    (2, "Yayında")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Sayfa Başlığı')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Adres URL')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='İçerik Sahibi')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True, verbose_name='İçerik')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='İçerik Statüsü')
    model_pic = models.ImageField(upload_to='uploads/', default='Görsel yükleyiniz...', verbose_name='İçerik Görseli')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # reply_to = models.ForeignKey('self', related_name='replies', null=True, blank=True)
    author = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    comment_image = models.ImageField(upload_to='uploads/', default='Görsel yükleyebilirsiniz...')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment