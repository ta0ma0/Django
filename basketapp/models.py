from django.db import models

from authapp.models import ShopUser
from firstapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE,
                             related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('количество', default=0)
    add_datetime = models.DateTimeField('время', auto_now_add=True)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        return sum(map(lambda x: x.quantity, self.user.basket.all()))

    @property
    def total_cost(self):
        return sum(map(lambda x: x.product_cost, self.user.basket.all()))

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)
