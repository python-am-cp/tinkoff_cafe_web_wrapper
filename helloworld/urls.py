from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from . import validation

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('', views.index_page, validation.valid('helloworld/input_user/')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)