from django.db import models
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from user.models import CustomUser
from ckeditor.fields import RichTextField
from ir_project.models import (Topic,Region)
# Create your models here.
class TopicArticle(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.TextField()
    image = models.ImageField(upload_to='article/')
    writer = models.CharField(max_length=250,null=True,blank=True)
    create_by = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    status = models.IntegerField(default=0)
    artice_content = RichTextField(config_name='awesome_ckeditor')
    slug = models.SlugField(unique=True,max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)

        if self.id:
            existing = get_object_or_404(TopicArticle,id=self.id)
            if existing.image != self.image:
                existing.image.delete(save=False)
        super(TopicArticle,self).save(*args, **kwargs)
    @receiver(pre_delete,sender = 'article.TopicArticle')
    def topic_article_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)
class Comment(models.Model):
    article = models.ForeignKey(TopicArticle,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.user_name

class TopicError(models.Model):
    topic = models.ForeignKey(TopicArticle,on_delete=models.CASCADE)
    tacher = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    error_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='event/')
    cheaf_guest = models.CharField(max_length=250)
    guest_details_info = RichTextField(config_name='awesome_ckeditor')
    event_content = RichTextField(config_name='awesome_ckeditor')
    status = models.IntegerField(default=0)
    event_date = models.DateField()
    event_start = models.TimeField()
    event_end = models.TimeField()
    slug = models.SlugField(unique=True,max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)

        if self.id:
            existing = get_object_or_404(Event,id=self.id)
            if existing.image != self.image:
                existing.image.delete(save=False)
        super(Event,self).save(*args, **kwargs)
    @receiver(pre_delete,sender = 'article.Event')
    def topic_article_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)
class Department(models.Model):
    name = models.CharField(max_length=200,unique=True)
    dept_code = models.CharField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class StudentSession(models.Model):
    name = models.CharField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class EventParticipate(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250,null=True,blank=True)
    phone_number = models.CharField(max_length=11)
    student_id = models.CharField(max_length=50,null=True,blank=True)
    student_year = models.CharField(max_length=150)
    student_dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    student_session = models.ForeignKey(StudentSession,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
