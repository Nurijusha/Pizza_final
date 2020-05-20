from django.urls import path

from .views import DiscountsDetail,DiscountsList


app_name = "cooks"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('',  DiscountsList.as_view()),
    path('<int:pk>/', DiscountsDetail.as_view()),
]
