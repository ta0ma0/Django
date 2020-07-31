"""geekshop URL Configuration"""

from django.contrib import admin
from django.urls import path, re_path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', basketapp.index, name='index'),
    re_path(r'^add/(?P<pk>\d+)/$', basketapp.add, name='add'),
    re_path(r'^delete/(?P<pk>\d+)/$', basketapp.delete, name='delete'),
    path('delete/product/<int:pk>/', basketapp.delete_product, name='delete_product'),
    re_path(r'^change/(?P<pk>\d+)/quantity/(?P<quantity>\d+)/$', basketapp.change),
]