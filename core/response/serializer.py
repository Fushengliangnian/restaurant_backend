from abc import ABC

from rest_framework import serializers


class ResponseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    code = serializers.IntegerField()
    message = serializers.CharField()
    result = serializers.BaseSerializer()
    requests_id = serializers.CharField()
