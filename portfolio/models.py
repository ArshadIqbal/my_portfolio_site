from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(
        upload_to='portfolio/images/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.title},{self.url}'


class Services(models.Model):
    title = models.CharField(max_length=15)
    fa_url = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'
