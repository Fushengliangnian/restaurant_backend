from rest_framework import mixins

from core.api.base import BaseGenericAPIView
from core.response.pagination import StandardResultsSetPagination
from shop.models import Goods
from shop.serializer import GoodsSerializer, GoodsListResponseSerializer


class GoodsListAPI(mixins.ListModelMixin, BaseGenericAPIView):
    # queryset = Goods.objects.all()
    queryset = [
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
        Goods(name="aaa", price=10, currency="积分", total=100, description="aaaaaaaaaaaaaaaa"),
    ]
    serializer_class = GoodsSerializer
    response_serializer_class = GoodsListResponseSerializer
    authentication_classes = []
    pagination_class = StandardResultsSetPagination

    def post(self, request, *args, **kwargs):
        print("-------------")
        return self.list(request, *args, **kwargs)


class GoodsDetailAPI(mixins.RetrieveModelMixin, BaseGenericAPIView):
    queryset = Goods.objects
    serializer_class = GoodsSerializer

    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
