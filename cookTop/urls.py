from django.urls import path

from .views import TopCooks


app_name = "cookTop"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', TopCooks.as_view(), name='topCooks'),
]
