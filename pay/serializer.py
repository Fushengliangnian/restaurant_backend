from rest_framework import serializers

from core.response.serializer import ResponseSerializer
from pay.models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"


class BillListResponseSerializer(ResponseSerializer):
    result = BillSerializer()
