# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2022/9/22 5:17 下午
# @Author  : lidong@test.com
# @Site    :
# @File    : urls.py
from django.urls import path

from integral.views import IntegralListAPI
from integral.views import IntegralDetailAPI


def temp_func():
    pass


urlpatterns = [
    path("statistics/list", IntegralListAPI.as_view()),
    path("gather/detail", IntegralDetailAPI.as_view()),
]
