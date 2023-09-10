from django.contrib import admin
from .models import (
    Region,
    Topic,
    Podcast,
    Interview
)
# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields ={"topic_slug":("name",),}


admin.site.register(Region)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Podcast)
admin.site.register(Interview)