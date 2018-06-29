# coding=utf-8

from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^$', views.login_view),
    url(r'top.html', views.top_view),
    url(r'left.html', views.left_view),
    url(r'center.html', views.center_view),
    url(r'down.html', views.down_view),




]