
from django.conf.urls import url
from django.urls import include

from blog import views

# SET THE NAMESPACE!
app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hakkimda/', views.about_me, name='aboutme'),
    url('blog/', views.Postlist, name='home'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetail, name='post_detail'),
    url(r'^test/', views.requestGet, name='requestGet')
]
