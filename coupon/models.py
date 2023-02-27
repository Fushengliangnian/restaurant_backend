from django.db import models

from core.model.base import BaseModel
from core.model.base import NotNullCharField
from customer.models import Customer


class Coupon(BaseModel):
    coupon_id = models.UUIDField(help_text="优惠券唯一ID")
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = NotNullCharField(help_text="优惠券名称")
    description = models.TextField(help_text="描述")
    available = models.BooleanField(help_text="是否可用")
    start_time = models.BooleanField(help_text="开始时间")
    expire_time = models.BooleanField(help_text="过期时间")
    amount = models.BooleanField(help_text="优惠券金额")
    amount_unit = models.BooleanField(help_text="优惠券金额单位")
    integral_value = models.BooleanField(help_text="积分值")

    class Meta:
        verbose_name = "优惠券记录表"
