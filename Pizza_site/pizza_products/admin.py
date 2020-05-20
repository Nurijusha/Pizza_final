from django.contrib import admin
from .models import *


class PizzaProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PizzaProduct._meta.fields]
    list_filter = ['price']
    class Meta:
        Model = PizzaProduct
class Pizza_commentAdmin(admin.ModelAdmin):
    list_display = ['user', 'pizza','text','date_added']
    list_filter = ['date_added']


admin.site.register(PizzaProduct, PizzaProductAdmin)
admin.site.register(pizza_comment, Pizza_commentAdmin)
