from django.conf.urls import url
from . import views
app_name='companies'
urlpatterns = [
url(r'^index/$',views.index,name='index'),
url(r'^post/new/$', views.transport_new, name='post_new'),
url(r'^detail/(?P<album_id>[0-9]+)/$', views.StockList1.as_view(), name='detail'),
url(r'^albdetail/(?P<album_id>[0-9]+)/$', views.albdetail, name='albdetail'),
url(r'^test/$', views.test, name='test'),
url(r'^service/$', views.service, name='service'),
url(r'^team/$', views.team, name='team'),
url(r'^problems/$', views.problems, name='problems'),
url(r'^contact/$', views.contact, name='contact'),
url(r'^login/$', views.login, name='login'),
]

