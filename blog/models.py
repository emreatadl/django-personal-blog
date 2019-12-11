from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"
        # slug

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


STATUS = (
    (0, "Taslak"),
    (1, "Yayına Hazır"),
    (2, "Yayında")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Sayfa Başlığı')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Adres URL')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='İçerik Sahibi')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True, verbose_name='İçerik')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='İçerik Statüsü')
    model_pic = CloudinaryField('image')
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_date',)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment
