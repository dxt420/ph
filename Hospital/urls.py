
from django.urls import path, include
from . import views

app_name = 'Hospital'

urlpatterns = [
    path('', views.home1, name='home1'),
    path('home1', views.home1, name='home1'),
    path('medcategory', views.medcategory, name='medcategory'),
    path('medinvent', views.medinvent, name='medinvent'),
    path('sales', views.sales, name='sales'),
    path('staff', views.staff, name='staff'),
    path('expense', views.expense, name='expense'),
    path('expensecategory', views.expensecategory, name='expensecategory'),

]
