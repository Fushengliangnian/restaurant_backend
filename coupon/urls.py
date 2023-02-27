from django.urls import path

from coupon.views import CouponListAPI
from coupon.views import CouponDetailAPI
from coupon.views import CouponVerifyAPI


def temp_func():
    pass


urlpatterns = [
    path("list/", CouponListAPI.as_view()),
    path("detail/", CouponDetailAPI.as_view()),
    path("verify", CouponVerifyAPI.as_view()),
]
