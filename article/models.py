from django.db import models
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from ckeditor.fields import RichTextField
from ir_project.models import (Topic)
# Create your models here.
class TopicArticle(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    title = models.TextField()
    image = models.ImageField(upload_to='article/')
    status = models.IntegerField(default=0)
    artice_content = RichTextField()
    slug = models.SlugField(unique=True)
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