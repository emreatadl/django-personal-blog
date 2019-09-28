from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'', views.analysis_index, name='demo'),
]