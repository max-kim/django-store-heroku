from django.core.management.base import BaseCommand
from catalog import models
import json
import os


class Command(BaseCommand):
    help = 'Create fish-data for demo store.'

    def handle(self, *args, **options):
        if len(models.Category.objects.all()):
            return 0

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_init_demo.json')) as file_stream:
            fish_data = json.load(file_stream)
        objects_dict = {'category': {}, 'product': {}, 'characteristic': {}}
        create_instances(models.Category, objects_dict, fish_data, 'category')
        create_instances(models.Characteristic, objects_dict, fish_data, 'characteristic')
        create_instances(models.Product, objects_dict, fish_data, 'product')
        create_instances(models.CharacteristicValue, objects_dict, fish_data, 'charact_value')
        create_instances(models.Comment, objects_dict, fish_data, 'comment')


def create_instances(obj_class, objects_dict: dict, fish_data, ident):
    for fields_dict in fish_data[ident]:
        instance = obj_class()
        for field, value in fields_dict.items():
            setattr(instance, field, objects_dict[field][value] if field in objects_dict.keys() else value)
        instance.save()
        if ident in objects_dict.keys():
            objects_dict[ident][instance.pk] = instance
