from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^todos/$', views.todo_list),
    url(r'^todos/(?P<pk>[0-9]+)/$', views.todo_detail),
]
