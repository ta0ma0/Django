from django.db import models

from authapp.models import ShopUser
from firstapp.models import Product


# class BasketQuerySet(models.QuerySet):  # own model manager
#     def delete(self):
#         for object in self:
#             # object.product.quantity += object.quantity
#             # object.product.save()
#             object.delete()
#         return super().delete()


class Basket(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE,
                             related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('количество', default=0)
    add_datetime = models.DateTimeField('время', auto_now_add=True)

    # objects = BasketQuerySet.as_manager()

    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        "return total quantity for user"
        # _items = Basket.objects.filter(user=self.user)
        # _items = self.user.basket_set.all()
        return sum(map(lambda x: x.quantity, self.user.basket.all()))
        # return sum(self.user.basket.values_list('quantity', flat=True))

    @property
    def total_cost(self):
        "return total cost for user"
        # _items = Basket.objects.filter(user=self.user)
        # _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return sum(map(lambda x: x.product_cost, self.user.basket.all()))

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     pass

    # def delete(self, using=None, keep_parents=False):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     return super().delete(using=None, keep_parents=False)