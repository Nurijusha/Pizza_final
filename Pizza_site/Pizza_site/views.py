from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def about_page(request):
    context = {
        "title": "About",
        "content": "This is the about page."
    }
    return render(request, "pizzeria/about_page.html", context)
