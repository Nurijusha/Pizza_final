from django.contrib import admin
from .models import Cook, Discounts

class CookAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    list_filter = ['name']

class DiscountsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','body','author','period']
    list_filter = ['title', 'period']

admin.site.register(Cook, CookAdmin)
admin.site.register(Discounts, DiscountsAdmin)
