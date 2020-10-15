# Generated by Django 3.1.1 on 2020-10-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chotihatti', '0003_auto_20201013_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='chunris',
            name='category',
            field=models.CharField(choices=[('Chunri', 'Chunri'), ('Dresses', 'Dresses'), ('Jewellery', 'Jewellery')], default='Chunri', max_length=25),
        ),
        migrations.AddField(
            model_name='dresses',
            name='category',
            field=models.CharField(choices=[('Chunri', 'Chunri'), ('Dresses', 'Dresses'), ('Jewellery', 'Jewellery')], default='Dresses', max_length=25),
        ),
        migrations.AddField(
            model_name='jewellery',
            name='category',
            field=models.CharField(choices=[('Chunri', 'Chunri'), ('Dresses', 'Dresses'), ('Jewellery', 'Jewellery')], default='Jewellery', max_length=25),
        ),
    ]