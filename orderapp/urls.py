from django.urls import path

import orderapp.views as orderapp

app_name = 'orderapp'

urlpatterns = [
    path('', orderapp.OrderList.as_view(), name='index'),
    path('order/create/', orderapp.OrderCreate.as_view(), name='order_create'),
    path('order/read/<int:pk>/', orderapp.OrderRead.as_view(), name='order_read'),
    path('order/update/<int:pk>/', orderapp.OrderUpdate.as_view(), name='order_update'),
    path('order/delete/<int:pk>/', orderapp.OrderDelete.as_view(), name='order_delete'),
    path('order/to/proceed/<int:pk>/', orderapp.order_to_proceed, name='order_to_proceed'),
]
