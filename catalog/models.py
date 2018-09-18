from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def to_slug_case(value: str) -> str:
    return '{}-{}'.format(slugify(value, allow_unicode=True), str(int(time())))


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, default=to_slug_case(str(title)))

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('category_url', kwargs={'category_slug': self.slug})


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, default=to_slug_case(str(title)))
    image = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('product_url', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})


class Characteristic(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return str(self.title)


class CharacteristicValue(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, db_index=True)


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.price)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    comment = models.TextField(blank=False)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
