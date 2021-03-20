from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView,TemplateView
from django.urls import reverse



from sales.forms import *



class SellMedicine(LoginRequiredMixin,FormView):
    template_name = 'sell/new_sell.html'
    form_class = MedicineTransactionForm
    success_url = '/sales/sale_medicine_report'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/sales/sale_medicine_report')

class SellMedicineReport(LoginRequiredMixin,TemplateView):
    template_name = 'sell/sell_item.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        kwargs['transactions'] = MedicineTransaction.objects.all()
        print(kwargs['transactions'])
        return kwargs

# @login_required
# def AutomateFile(request):

