from django.db import models


def to_slug_case(value: str) -> str:
    value = value.replace(' ', '_')
    value = value.replace('.', '_')
    value = value.replace(',', '_')
    value = value.replace('/', '_')
    value = value.replace('\\', '_')
    value = value.replace('*', '_')
    value = value.replace('+', '_')
    value = value.replace('=', '_')
    value = value.replace(':', '_')
    value = value.replace(';', '_')
    return value.lower()


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return '{}'.format(self.title)


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, default=to_slug_case(str(title)))
    price = models.FloatField(default=0.00, )

    def __str__(self):
        return '{}'.format(self.title)


class Characteristic(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.category, self.title)


class CharacteristicValue(models.Model):
    characteristic =
