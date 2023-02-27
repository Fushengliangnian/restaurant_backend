from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.base import BaseGenericAPIView


class IntegralListAPI(mixins.RetrieveModelMixin, BaseGenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class IntegralDetailAPI(mixins.RetrieveModelMixin, BaseGenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CouponVerifyAPI(mixins.RetrieveModelMixin, BaseGenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
