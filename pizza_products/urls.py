from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pizza/<int:pk>/', views.pizza_detail, name='pizza-detail'),
    path('pizza/pizzacomments/<int:pk>/', views.add_comment, name= 'pizzacomments'),

]
