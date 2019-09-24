from django.db import models

CATEGORY_CHOICES = (
    ('телефоны', 'smartphones'),
    ('весы', 'weights'),
    ('сувениры', 'souvenirs'),
    ('иное', 'others')
)


class Product(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False, verbose_name='наименование товара')
    description = models.TextField(max_length=2000, blank=True, default='', verbose_name='описание')
    category = models.CharField(max_length=40, null=False, blank=False, verbose_name="Статус",
                                default=CATEGORY_CHOICES[0][0], choices=CATEGORY_CHOICES)
    balance = models.PositiveIntegerField(blank=True, verbose_name = "остаток")

    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name='цена')

    def __str__(self):
        return self.description
