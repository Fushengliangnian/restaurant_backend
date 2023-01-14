# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2022/9/22 5:17 下午
# @Author  : lidong@test.com
# @Site    :
# @File    : urls.py
from django.urls import path

from shop.views import GoodsListAPI


def temp_func():
    pass

urlpatterns = [
    path("goods/list", GoodsListAPI.as_view()),
    path("goods/detail", GoodsListAPI.as_view()),
]
