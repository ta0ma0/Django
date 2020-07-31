from random import random

from django.http import request, JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from firstapp.models import ProductCategory, Product

# Create your views here.
from basketapp.models import Basket


def get_menu():
    return ProductCategory.objects.all()


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket.all()
    else:
        return []


def get_hot_product():
    return random.choice(Product.objects.all())


def get_same_products(hot_product):
    return hot_product.category.product_set.exclude(pk=hot_product.pk)


def index(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()[:16]
    context = {
        'page_title': 'главная',
        'categories': categories,
        'products': products,
        'basket': get_basket(request),
    }
    return render(request, 'firstapp/index.html', context)


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    context = {
        'page_title': 'продукты',
        'categories': categories,
        'products': products,
        'basket': get_basket(request)

    }
    return render(request, 'firstapp/product-range.html', context)


def contacts(request):
    context = {
        'page_title': 'контакты'
    }
    return render(request, 'firstapp/contacts.html', context)


def probe_images(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'probe_images': 'probe_images',
    }
    return render(request, 'firstapp/test_images.html', context)

def category(request, pk):
    categories = ProductCategory.objects.all()

    if pk == '0':
        category = {'pk': 0, 'name': 'Все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.all()

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'firstapp/categories_products.html', context)

def product(request, pk):
    context = {
        'page_title': 'продукт',
        'product': get_object_or_404(Product, pk=pk),
        'catalog_menu': get_menu(),
        'basket': get_basket(request),
    }

    return render(request, 'firstapp/product.html', context)


def product_detail_async(request, pk):
    if request.is_ajax():
        try:
            product = Product.objects.get(pk=pk)
            return JsonResponse({
                'product_price': product.price,
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            })