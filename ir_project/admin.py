from django.contrib import admin
from .models import (
    Region,
    Topic,
    Podcast,
    Interview
)
# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("name",),}
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("name",),}
class PodcastAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("name",),}

class InterviewAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("name",),}

admin.site.register(Region,RegionAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Podcast,PodcastAdmin)
admin.site.register(Interview,InterviewAdmin)