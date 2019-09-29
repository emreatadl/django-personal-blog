from django.conf.urls import url
from django.urls import include
from blog import views
from django.conf.urls import handler500, handler404

# SET THE NAMESPACE!
app_name = 'blog'

urlpatterns = [
    url(r'^hakkimda/', views.about_me, name='aboutme'),
    url('blog/', views.Postlist, name='home'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetail, name='post_detail'),
    url(r'^kategori/(?P<slug>[-\w]+)/$', views.category_list, name='category'),
]