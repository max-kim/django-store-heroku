# Generated by Django 2.1.1 on 2018-09-20 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180920_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteristicvalue',
            options={'ordering': ['characteristic__id']},
        ),
    ]