from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('request_page/', views.directComputationReq, name="request_pg"),
    path('', views.index_page, name='index'),
    path('form_send/', views.uploadFiles, name="form_snd")
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)