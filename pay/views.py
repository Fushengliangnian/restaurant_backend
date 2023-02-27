from django.db.models import Sum
from rest_framework import mixins

from core.api.base import BaseGenericAPIView
from core.response.pagination import StandardResultsSetPagination
from pay.models import Bill
from pay.serializer import BillSerializer
from pay.serializer import BillListResponseSerializer


class BillListAPI(mixins.ListModelMixin, BaseGenericAPIView):
    # queryset = Bill.objects.all()
    queryset = [
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
        Bill(remake="11111111111", user_id=1, coupon_id=1),
    ]
    serializer_class = BillSerializer
    response_serializer_class = BillListResponseSerializer
    authentication_classes = []
    pagination_class = StandardResultsSetPagination

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BillGatherAPI(BaseGenericAPIView):
    def post(self, request, *args, **kwargs):
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        Bill.objects.filter(
            user=self.request.user,
            create_time__gte=start_time,
            create_time__lte=end_time
        ).aggregate(price_sum=Sum("price"))
        return


class BillDetailAPI(BaseGenericAPIView):
    def post(self, request, *args, **kwargs):
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        Bill.objects.filter(
            user=self.request.user,
            create_time__gte=start_time,
            create_time__lte=end_time
        ).aggregate(price_sum=Sum("price"))
        return
