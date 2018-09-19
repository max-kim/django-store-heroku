from django.contrib import admin
from .models import Category, Product, Characteristic, CharacteristicValue, Comment


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Characteristic)
admin.site.register(CharacteristicValue)
admin.site.register(Comment)
