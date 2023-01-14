from django.shortcuts import render
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.base import BaseGenericAPIView


class LoginAPIView(APIView):
    def post(self, request):
        return Response({})


class CustomerInfoDetailAPI(mixins.RetrieveModelMixin, BaseGenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
