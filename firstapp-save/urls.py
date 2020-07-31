"""geekshop URL Configuration"""

from django.contrib import admin
from django.urls import path, re_path
import firstapp.views as firstapp
app_name = 'firstapp'
urlpatterns = [
    path('', firstapp.index, name='index'),
    path('products/', firstapp.products, name='products'),
    path('contacts/', firstapp.contacts, name='contacts'),
    path('probe_images/', firstapp.probe_images, name='probe_images'),
    re_path('category/(?P<pk>\d+)', firstapp.category, name='category'),
    re_path(r'^product/(?P<pk>\d+)/$', firstapp.product, name='product'),
    re_path(r'^product/detail/(?P<pk>\d+)/async/$', firstapp.product_detail_async),
    path('admin/', admin.site.urls),
]