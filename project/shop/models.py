from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    id = models.BigIntegerField(verbose_name='Айди', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Назва', max_length=255, unique=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категорія'
        verbose_name_plural = 'категорії'


class Product(models.Model):
    id = models.BigIntegerField(verbose_name='Айди', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Назва', max_length=255)
    description = RichTextField(verbose_name='Опис')
    price = models.BigIntegerField(verbose_name='Ціна')
    category = models.ForeignKey(verbose_name='Категорія', to=Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукти'


class Order(models.Model):
    id = models.BigIntegerField(verbose_name='Айди', primary_key=True, unique=True)
    product = models.ForeignKey(verbose_name='Товар', to=Product, on_delete=models.SET_NULL, null=True)
    number = models.CharField(verbose_name='Телефон користувача', max_length=255)
    email = models.CharField(verbose_name='Email користувача', max_length=255)
    address = models.TextField(verbose_name='Адреса доставки')
    is_completed = models.BooleanField(verbose_name='Прапорець “виконання”')
    created_date = models.DateTimeField(verbose_name='Дата створення замовлення', auto_now_add=True)

    class Meta:
        verbose_name = 'замовлення'
        verbose_name_plural = 'замовлення'

