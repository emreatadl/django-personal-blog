from django.contrib import admin
from django.urls import *
from django.conf.urls import url,include
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('ea/kp/admin/', include('material.admin.urls')),
    url(r'', include('blog.urls')),
    path(r'analiz/', include('analysis.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)