from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Game(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/')
    review = CKEditor5Field('Text', config_name='extends')

    screenshots = models.JSONField(default=list, blank=True)  # or use separate model if you want uploads

    download_link_1 = models.URLField(max_length=500, blank=True, null=True)
    download_link_2 = models.URLField(max_length=500, blank=True, null=True)
    download_link_3 = models.URLField(max_length=500, blank=True, null=True)

    pros = models.JSONField(default=list, blank=True)   # List of strings
    cons = models.JSONField(default=list, blank=True)   # List of strings

    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='post_images/')
    content = CKEditor5Field('Text', config_name='extends')
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title
