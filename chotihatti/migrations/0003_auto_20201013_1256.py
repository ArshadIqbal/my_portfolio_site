# Generated by Django 3.1.1 on 2020-10-13 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chotihatti', '0002_newarrivals_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chunris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('rating', models.IntegerField(default=5)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(100000)])),
                ('pieces', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='chotihatti/images/chunris')),
                ('date_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('rating', models.IntegerField(default=5)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(100000)])),
                ('pieces', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='chotihatti/images/dress')),
                ('date_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jewellery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('rating', models.IntegerField(default=5)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(100000)])),
                ('pieces', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='chotihatti/images/jewellery')),
                ('date_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='NewArrivals',
        ),
    ]