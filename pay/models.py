from django.db import models

from core.model.base import BaseModel
from core.model.base import NotNullCharField
from customer.models import Customer
from coupon.models import Coupon


class Bill(BaseModel):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True)
    extra_discount_price = models.IntegerField(help_text="额外的折扣价格")
    remake = models.TextField(help_text="备注")

    class Meta:
        verbose_name = "账单记录表"


class BillItem(BaseModel):
    name = NotNullCharField(help_text="账单项的名称")
    price = models.IntegerField(help_text="单价")
    count = models.IntegerField(help_text="数量")
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name="bill_relation")
