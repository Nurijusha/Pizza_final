from django.contrib import admin
from .models import Order, ItemInOrder


class OrderItemInline(admin.TabularInline):
    model = ItemInOrder
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'first_name', 'last_name', 'email', 'address', 'number', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)