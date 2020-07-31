from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from basketapp.models import Basket
from firstapp.models import Product

from firstapp.models import ProductCategory


def get_menu():
    return ProductCategory.objects.all()


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket.all()
    else:
        return []


@login_required
def index(request):
    return render(request, 'basketapp/index.html')


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main:category',
                                            kwargs={
                                                'pk': pk
                                            }))

    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()
    return HttpResponseRedirect(reverse('basket:index'))


@login_required
def delete_product(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()
    return HttpResponseRedirect(reverse('basket:index'))


@login_required
def change(request, pk, quantity):
    quantity = int(quantity)
    if request.is_ajax():
        basket = get_object_or_404(Basket, pk=pk)
        if quantity <= 0:
            basket.delete()
        else:
            basket.quantity = quantity
            basket.save()


        result = render_to_string(
            'basketapp/includes/inc__basket_list.html',

            request=request
        )

        return JsonResponse({'result': result})


