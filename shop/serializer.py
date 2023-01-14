from rest_framework import serializers

from core.response.serializer import ResponseSerializer
from shop.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"


class GoodsListResponseSerializer(ResponseSerializer):
    result = GoodsSerializer()
