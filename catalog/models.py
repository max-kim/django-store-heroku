from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def to_slug_case(value: str) -> str:
    return '{}-{}'.format(slugify(value, allow_unicode=True), str(int(time())))


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_breadcrumbs(self):
        return [self.title, ]

    def get_absolute_url(self):
        return reverse('category_url', kwargs={'pk': self.id})


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(default=0.00)
    rating = models.FloatField(default=0.00)
    image = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

    def get_breadcrumbs(self):
        return [self.category, self.title]

    def get_absolute_url(self):
        return reverse('product_url', kwargs={'category__pk': self.category.id, 'pk': self.id})


class Characteristic(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return str(self.title)


class CharacteristicValue(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')
    value = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return '{}: {} - {}'.format(self.product, self.characteristic, self.value)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='comments')
    comment = models.TextField(blank=False)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
