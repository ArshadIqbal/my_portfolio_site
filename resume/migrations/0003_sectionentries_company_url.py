# Generated by Django 3.1.1 on 2020-09-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_sectionentries'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionentries',
            name='company_url',
            field=models.URLField(blank=True),
        ),
    ]