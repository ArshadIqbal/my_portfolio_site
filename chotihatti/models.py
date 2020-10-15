from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

Category = (
    ('Chunri', 'Chunri'),
    ('Dresses', 'Dresses'),
    ('Jewellery', 'Jewellery'),
)


class NewArrivals(models.Model):
    category = models.CharField(
        max_length=25, choices=Category, blank=False, null=False)
    title = models.CharField(max_length=150, blank=True, null=True)
    rating = models.IntegerField(default=5)
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(100000)])
    image = models.ImageField(
        upload_to='chotihatti/images/', null=True, blank=True)

    def __str__(self):
        return f'{self.category}, {self.title}, {self.price}, {self.rating}'


class Chunris(models.Model):
    category = models.CharField(
        max_length=25, choices=Category, default='Chunri', blank=False, null=False)
    title = models.CharField(max_length=150, blank=True, null=True)
    rating = models.IntegerField(default=5)
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(100000)])
    pieces = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)])
    image = models.ImageField(
        upload_to='chotihatti/images/', null=True, blank=True)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.category},{self.title}, {self.price}, {self.pieces}, {self.rating},{self.date_added}'


class Jewellery(models.Model):
    category = models.CharField(
        max_length=25, choices=Category, default='Jewellery', blank=False, null=False)
    title = models.CharField(max_length=150, blank=True, null=True)
    rating = models.IntegerField(default=5)
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(100000)])
    pieces = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)])
    image = models.ImageField(
        upload_to='chotihatti/images/jewellery', null=True, blank=True)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.category},{self.title}, {self.price}, {self.pieces}, {self.rating},{self.date_added}'


class Dresses(models.Model):
    category = models.CharField(
        max_length=25, choices=Category, default='Dresses', blank=False, null=False)
    title = models.CharField(max_length=150, blank=True, null=True)
    rating = models.IntegerField(default=5)
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(100000)])
    pieces = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)])
    image = models.ImageField(
        upload_to='chotihatti/images/dress', null=True, blank=True)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.category},{self.title}, {self.price}, {self.pieces}, {self.rating},{self.date_added}'
