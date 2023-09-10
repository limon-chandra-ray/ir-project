from django.db import models
from django.utils.text import slugify
# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=250,unique=True)
    topic_slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="topic/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.topic_slug = slugify(self.name)
        super().save(*args, **kwargs)


class Region(models.Model):
    name = models.CharField(max_length=100,unique=True)
    region_slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="region/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.region_slug = slugify(self.name)
        super().save(*args, **kwargs)

class Podcast(models.Model):
    name = models.CharField(max_length=100,unique=True)
    podcast_slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="podcast/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.podcast_slug = slugify(self.name)
        super().save(*args, **kwargs)

class Interview(models.Model):
    name = models.CharField(max_length=100,unique=True)
    interview_slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="interview/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.interview_slug = slugify(self.name)
        super().save(*args, **kwargs)