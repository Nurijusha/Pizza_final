from django.shortcuts import render
from .models import Cook,Recommendation
from django.views.generic import ListView


class TopCooks(ListView):
    model = Recommendation
    template_name = 'topCooks.html'
    context_object_name = 'rec'
