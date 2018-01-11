from django.conf.urls import url

from todo import views

urlpatterns = [
    url(r'^todos/$', views.todo_list,name='todolist'),
    url(r'^todos/(?P<pk>[0-9]+)/$', views.todo_detail,name='tododetail'),
    url(r'^web/$', views.web_list ,name='weblist'),
    url(r'^web/new/$', views.web_new ,name='webnew'),
    url(r'^web/(?P<pk>[0-9]+)/$', views.web_detail ,name='webdetail'),

]
