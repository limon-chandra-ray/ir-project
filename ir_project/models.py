from django.db import models
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.db.models.signals import pre_delete
# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="topic/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)

        if self.id:
            existing = get_object_or_404(Topic,id = self.id)
            if existing.image != self.image:
                existing.image.delete(save=False)
        super(Topic,self).save(*args, **kwargs)
    @receiver(pre_delete,sender = "ir_project.Topic")
    def topic_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save=False)

class Region(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="region/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        if self.id:
                existing = get_object_or_404(Region,id = self.id)
                if existing.image != self.image:
                    existing.image.delete(save=False)
        super(Region,self).save(*args, **kwargs)
    @receiver(pre_delete,sender = "ir_project.Region")
    def region_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save=False)

class Podcast(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="podcast/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        if self.id:
            existing = get_object_or_404(Podcast,id = self.id)
            if existing.image != self.image:
                existing.image.delete(save=False)
        super(Podcast,self).save(*args, **kwargs)
    @receiver(pre_delete,sender = "ir_project.Podcast")
    def podcast_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save=False)

class Interview(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="interview/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.name_slug = slugify(self.name)

        if self.id:
            existing = get_object_or_404(Interview,id = self.id)
            if existing.image != self.image:
                existing.image.delete(save=False)
        super(Interview,self).save(*args, **kwargs)

    @receiver(pre_delete,sender = "ir_project.Interview")
    def interview_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save=False)