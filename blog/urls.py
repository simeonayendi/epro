from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^post_list/$', views.post_list, name="post_list"),
    url(r'^news/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail, name="post_detail"),

]
