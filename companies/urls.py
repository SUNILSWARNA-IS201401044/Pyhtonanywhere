from django.conf.urls import url
from . import views
app_name='companies'
urlpatterns = [
url(r'^index/$',views.index,name='index'),
url(r'^post/new/$', views.transport_new, name='post_new'),
]

