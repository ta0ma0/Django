from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # path('', adminapp.index, name='index'),
    path('', adminapp.ShopUserList.as_view(), name='index'),

    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('user/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('category/list/', adminapp.categories, name='categories'),

    # path('category/create/', adminapp.category_create, name='category_create'),
    path('category/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),

    # path('category/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('category/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(),
         name='category_update'),

    # path('category/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),
    path('category/delete/<int:pk>/', adminapp.ProductCategoryDelete.as_view(), name='category_delete'),

    path('category/<int:pk>/products/', adminapp.category_products, name='category_products'),

    path('category/<int:category_pk>/product/create/', adminapp.product_create, name='product_create'),
    # path('product/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('product/read/<int:product_pk>/', adminapp.ProductDetail.as_view(), name='product_read'),

    path('product/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('product/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
]
