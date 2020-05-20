from django.contrib import admin
from .models import News, Rate, Review

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','text','img', 'author', 'date']
    list_filter = ['id', 'date', 'author']
    search_fields = ['text', 'title']
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'post','text','date']
    list_filter = ['date']
admin.site.register(News, NewsAdmin)
admin.site.register(Review, ReviewAdmin)
