from django.contrib import admin
from .models import TopicArticle
# Register your models here.


class TopicArticleAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("title",),}

admin.site.register(TopicArticle,TopicArticleAdmin)