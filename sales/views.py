from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView 


class SellMedicine(LoginRequiredMixin,TemplateView):
    template_name = 'sell/sell_item.html'