from django.db import models

from core.model.base import BaseModel


class Customer(BaseModel):
    open_id = models.CharField(max_length=255, help_text="微信唯一ID", verbose_name="微信唯一ID")
    nickname = models.CharField(max_length=255, help_text="微信昵称", verbose_name="微信昵称")
    sex = models.IntegerField(choices=((1, "男"), (2, "女"), (0, "未知")), help_text="性别", verbose_name="性别")
    country = models.CharField(max_length=100, help_text="国家", verbose_name="国家")
    province = models.CharField(max_length=100, help_text="省份", verbose_name="省份")
    city = models.CharField(max_length=100, help_text="城市", verbose_name="城市")
    head_img_url = models.TextField(help_text="用户头像地址", verbose_name="用户头像地址")

    mobile_phone = models.CharField(max_length=100, help_text="手机号码", verbose_name="手机号码")
    email = models.CharField(max_length=255, help_text="邮箱", verbose_name="邮箱")

    class Meta:
        verbose_name = "客户表"

