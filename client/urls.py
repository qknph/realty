# coding=utf-8

from django.conf.urls import url

from client import views

urlpatterns = [

    url(r'customer_list1.html', views.customer_list1),
    url(r'customer_distribute_list.html', views.customer_distribute_list),
    url(r'customer_care_list.html', views.customer_care_list),
    url(r'customer_type_list.html', views.customer_type_list),
    url(r'customer_state_list.html', views.customer_state_list),
    url(r'customer_source_list.html', views.customer_source_list),

]