from django.contrib import admin
from django.urls import *
from django.conf.urls import url,include
from emreatadil.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^$', index, name='index'),
]
