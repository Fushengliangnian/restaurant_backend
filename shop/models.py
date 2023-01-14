from django.db import models

from core.model.base import BaseModel
from core.model.base import NotNullCharField
from core.model.base import NullCharField


class Goods(BaseModel):
    name = NotNullCharField(help_text="商品名称")
    price = models.IntegerField(help_text="价格的数值")
    currency = NotNullCharField(help_text="货币符号")
    total = models.IntegerField(null=True, help_text="库存总数")
    description = models.TextField(help_text="描述")
    thumbnail = NullCharField(max_length=500, help_text="商品的缩略图地址")
