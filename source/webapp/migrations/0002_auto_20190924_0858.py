# Generated by Django 2.1 on 2019-09-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('телефоны', 'smartphones'), ('весы', 'weights'), ('сувениры', 'souvenirs'), ('иное', 'others')], default='телефоны', max_length=40, verbose_name='Категория'),
        ),
    ]