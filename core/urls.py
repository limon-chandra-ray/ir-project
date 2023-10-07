
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("",include("bcga.urls",namespace='bcga')),
    path('ir/',include("ir_project.urls",namespace='ir_project')),
    path('article/',include("article.urls",namespace='article')),
    path('student/',include("studentTeam.urls",namespace='studentTeam')),
    path('teacher/',include("teacherTeam.urls",namespace='teacherTeam')),
    path('super-admin/',include('sadmin.urls',namespace='sadmin'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
