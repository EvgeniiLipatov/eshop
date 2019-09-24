from django import forms
from django.forms import widgets

from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Наименование товара')
    description = forms.CharField(max_length=2000,label='Описание товара',widget=widgets.Textarea)
    category = forms.ChoiceField(required=True, label='Категория', choices=CATEGORY_CHOICES)
    balance = forms.IntegerField(label="остаток")
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label="цена")