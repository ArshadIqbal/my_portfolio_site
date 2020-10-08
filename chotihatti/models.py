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
