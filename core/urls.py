from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import Userprofile_api,user,Department_api,project_api,document_api,Projectsite_api, Summary_api,Celerytask,Downloadfile




urlpatterns = [
   path("",user,name='user'),
   path("userprofile/",Userprofile_api, name='userprofile'),
   path("userprofile/<int:pk>/",Userprofile_api,name='pk_userprofile'),
   path("department/",Department_api.as_view(), name='deparments'),
   path("department/<int:pk>/",Department_api.as_view(), name='pk_departments'),
   path("project/",project_api.as_view(), name='projects'),
   path("project/<int:pk>/",project_api.as_view(), name='pk_projects'),
   path("document/",document_api.as_view(), name='documents'),
   path("documents/<int:pk>/",document_api.as_view(), name='pk_documents'),
   path('projectsite/',Projectsite_api.as_view(), name='project_site'),
   path('downloadfile/<int:project_id>/',Downloadfile.as_view(), name='uploaded-file'),
   path('summary/',Summary_api.as_view(), name='summary'),
   path('celery/', Celerytask, name='celeryy'),
   path('auth/', include('rest_framework.urls',namespace='rest_framework')),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)