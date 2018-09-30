from django.core.management.base import BaseCommand
from catalog import models
import json
import os


class Command(BaseCommand):
    help = 'Create fish-data for demo store.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('Initializing django demo store data:'))
        if len(models.Category.objects.all()):
            self.stdout.write(self.style.HTTP_SUCCESS('  the storage data already exists!'))
            return 0

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_init_demo.json')) as file_stream:
            fish_data = json.load(file_stream)
        objects_dict = {'category': {}, 'product': {}, 'characteristic': {}}
        self.create_instances(models.Category, objects_dict, fish_data, 'category')
        self.create_instances(models.Characteristic, objects_dict, fish_data, 'characteristic')
        self.create_instances(models.Product, objects_dict, fish_data, 'product')
        self.create_instances(models.CharacteristicValue, objects_dict, fish_data, 'charact_value')
        self.create_instances(models.Comment, objects_dict, fish_data, 'comment')

    def create_instances(self, obj_class, objects_dict: dict, fish_data, ident):
        self.stdout.write('  processing - {}'.format(ident))
        for fields_dict in fish_data[ident]:
            instance = obj_class()
            for field, value in fields_dict.items():
                setattr(instance, field, objects_dict[field][value] if field in objects_dict.keys() else value)
            instance.save()
            if ident in objects_dict.keys():
                objects_dict[ident][instance.pk] = instance
        self.stdout.write(self.style.SUCCESS('  done!'))
