
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("bcga.urls",namespace='bcga')),
    path('ir',include("ir_project.urls",namespace='ir_project')),
    path('article/',include("article.urls",namespace='article')),
    path('student-team/',include("studentTeam.urls",namespace='studentTeam'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
