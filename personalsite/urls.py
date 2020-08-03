from django.conf import settings
from django.conf.urls import url, handler500, handler404
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
                  path('admin/', include('material.admin.urls')),
                  url(r'', include('blog.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
