from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
import os
from django.urls import reverse

 
def create_id():
    return get_random_string(22)
 
 
def upload_image_to(instance, filename):
    article_id = instance.id
    return os.path.join('static', 'items', item_id, filename)

 
class Tag(models.Model):
    slug = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=32)
 
    def __str__(self):
        return self.name

class Category(models.Model):
    slug = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=32)
 
    def __str__(self):
        return self.name
 
 
class Article(models.Model):
    id = models.CharField(default=create_id, primary_key=True,
                          max_length=22, editable=False)
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='', blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="", blank=True,
                              upload_to=upload_image_to)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_list')
