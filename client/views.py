# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def customer_list1(request):
    return render(request, 'customer_list1.html')


def customer_distribute_list(request):
    return render(request, 'customer_distribute_list.html')


def customer_care_list(request):
    return render(request, 'customer_care_list.html')


def customer_type_list(request):
    return render(request, 'customer_type_list.html')


def customer_state_list(request):
    return render(request, 'customer_state_list.html')


def customer_source_list(request):
    return render(request, 'customer_source_list.html')