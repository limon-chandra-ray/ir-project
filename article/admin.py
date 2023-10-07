from django.contrib import admin
from .models import TopicArticle,Event,Comment,Department,StudentSession
# Register your models here.


class TopicArticleAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("title",),}

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("title",),}

admin.site.register(Comment)
admin.site.register(Department)
admin.site.register(StudentSession)
admin.site.register(Event,EventAdmin)
admin.site.register(TopicArticle,TopicArticleAdmin)