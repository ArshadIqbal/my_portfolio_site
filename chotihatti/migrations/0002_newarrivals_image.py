# Generated by Django 3.1.1 on 2020-10-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chotihatti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newarrivals',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chotihatti/images/'),
        ),
    ]
