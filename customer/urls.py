# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2022/9/22 5:17 下午
# @Author  : lidong@test.com
# @Site    :
# @File    : urls.py
from django.urls import path

from customer.views import LoginAPIView
from customer.views import CustomerInfoDetailAPI


def temp_func():
    pass


urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("register/", LoginAPIView.as_view()),
    path("info/detail", CustomerInfoDetailAPI.as_view()),
    path("integral/", LoginAPIView.as_view()),
]
