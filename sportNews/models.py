from django.db import models
from tinymce.models import HTMLField

from .define import *
from .custom_field import *
from .helpers import *
# Create your models here.


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = CustomBooleanField()
    layout = models.CharField(
        max_length=10, choices=APP_VALUE_LAYOUT_CHOICES, default=APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(
        max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_LAYOUT_DEFAULT)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = TABLE_CATEGORY_SHOW

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(
        max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_LAYOUT_DEFAULT)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    publish_date = models.DateTimeField()
    content = HTMLField(default="No content")
    image = models.ImageField(upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = TABLE_ARTICLE_SHOW

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.content = clean_html(self.content)
        super().save(*args, **kwargs)
    
class Feed(models.Model):
    
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(
        max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_LAYOUT_DEFAULT)
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)
    
    class Meta:
        verbose_name_plural = TABLE_FEED_SHOW

    def __str__(self):
        return self.name
