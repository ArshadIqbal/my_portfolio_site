# Generated by Django 3.1.1 on 2020-09-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_sectionentries_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionentries',
            name='category',
            field=models.CharField(blank=True, choices=[('Experience', 'Experience'), ('Education', 'Education'), ('Certificatoins', 'Certifications'), ('Languages', 'Languages')], max_length=25, null=True),
        ),
    ]