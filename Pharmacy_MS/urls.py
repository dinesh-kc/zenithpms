
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from manage_medicines.views import medicine_manage, medicine_update,medicine_delete
from manageSaes_cash.views import sales_cash
from manageSaes_credit.views import sales_credit
from viewSales_Cash.views import viewSales_Cash
from viewSales_Credit.views import viewSales_Credit
from orderMedicine.views import orderMedicine
from automateFile.views import automateFile
from viewUsers.views import viewUsers

from django.contrib.auth.decorators import login_required
from .views import *

@login_required
def dashboard(request):
    return render(request, 'base.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard),
    path('accounts/',include('django.contrib.auth.urls')),
    path('sales/',include('sales.urls')),
    path('home', dashboard),
    path("register/", register, name="register"),
    path("register_view/", register_view, name="register_view"),
    # path("logout/", logout, name="logout"),






    path('manage_medicine', medicine_manage),
    path('sales_cash', sales_cash),
    path('sales_credit', sales_credit),
    path('viewSales_Cash', viewSales_Cash),
    path('viewSales_Credit', viewSales_Credit),
    path('orderMedicine', orderMedicine),
    path('automateFile', automateFile),
    # path('viewUsers', viewUsers),
    path('medicine_update/<int:id>', medicine_update),
    path('medicine_delete/<int:id>', medicine_delete),

    

]
