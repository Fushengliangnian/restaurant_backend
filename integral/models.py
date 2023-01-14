from django.db import models

from core.model.base import BaseModel
from customer.models import Customer


class Integral(BaseModel):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "积分表"
