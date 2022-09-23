# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2022/9/22 5:17 下午
# @Author  : lidong@test.com
# @Site    :
# @File    : urls.py
from django.urls import path


def temp_func():
    pass


urlpatterns = [
    path("wechat/callback/", temp_func),
    path("register/", temp_func),
    path("info/", temp_func),
    path("integral/", temp_func),
]
