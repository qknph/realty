# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def login_view(request):

    return render(request, 'index.html')


def top_view(request):
    return render(request, 'top.html')


def left_view(request):
    return render(request, 'left.html')


def center_view(request):
    return render(request, 'center.html')


def down_view(request):
    return render(request, 'down.html')




#
# def customer_distribute_list(request):
#     return render(request, 'customer_distribute_list.html')
#
#
# def customer_care_list(request):
#     return render(request, 'customer_care_list.html')
#
#
# def customer_type_list(request):
#     return render(request, 'customer_type_list.html')
#
#
# def customer_state_list(request):
#     return render(request, 'customer_state_list.html')
#
#
# def customer_source_list(request):
#     return render(request, 'customer_source_list.html')