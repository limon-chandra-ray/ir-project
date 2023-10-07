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

    def __str__(self):
        return self.name

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

class UserContact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    contact_sub = models.CharField(max_length=250)
    contact_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.first_name +" "+ self.last_name
    

class UserSubcribe(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.first_name +" "+ self.last_name
    
class Gallery(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def save(self,*args, **kwargs):

        if self.id:
            existing = get_object_or_404(Gallery,id = self.id)
            if existing.image != self.image:
                existing.image.delete(save=False)
        super(Gallery,self).save(*args, **kwargs)

    @receiver(pre_delete,sender = "ir_project.Gallery")
    def gallery_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save=False)

    