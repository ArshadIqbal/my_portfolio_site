# Generated by Django 3.1.1 on 2020-09-11 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_sectionentries_category_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionentries',
            name='category_new',
        ),
    ]
