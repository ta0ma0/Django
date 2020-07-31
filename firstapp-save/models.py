from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Имя категории', max_length=64)
    description = models.TextField('Описание категорий', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 verbose_name='Категория продукта',
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField('Краткое описание продукта', max_length=64, blank=True)
    description = models.TextField('Описание продукта', blank=True)
    price = models.DecimalField('Цена продукта', max_digits=8, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField('Количество на складе', default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

