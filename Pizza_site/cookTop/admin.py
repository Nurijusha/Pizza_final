from django.contrib import admin
from .models import Cook, Recommendation

class CookAdmin(admin.ModelAdmin):
    list_display = ['user', 'img', 'urlfield']
    list_filter = ['user']
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','pizza','body']
admin.site.register(Cook, CookAdmin)
admin.site.register(Recommendation, RecommendationAdmin)

# Register your models here.
