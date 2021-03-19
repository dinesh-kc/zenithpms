
from django.urls import path,include

from .views import *

urlpatterns = [
    path('sale_medicine', SellMedicine.as_view(),name='sell_medicine'),
    
]
