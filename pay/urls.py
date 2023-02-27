# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2022/9/22 5:17 下午
# @Author  : lidong@test.com
# @Site    :
# @File    : urls.py
from django.urls import path

from pay.views import BillListAPI
from pay.views import BillGatherAPI
from pay.views import BillDetailAPI


def temp_func():
    pass


urlpatterns = [
    path("wechat/callback/", temp_func),
    path("bill/list", BillListAPI.as_view()),
    path("bill/gather", BillGatherAPI.as_view()),
    path("bill/detail", BillDetailAPI.as_view()),
    path("integral/", temp_func),
]
