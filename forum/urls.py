from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^forum/$', views.forum, name="forum"),
    url(r'^group_create/$', views.group_create, name="group-create"),
    url(r'^forum/(?P<slug>[\w-]+)/$', views.forum_list, name="forum_list"),
    url(r'^event$', views.event, name="event"),

]
