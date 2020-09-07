from django.db import models
from django_countries.fields import CountryField

class IndexSlider(models.Model):
    greetings = models.CharField(max_length=50)
    title_bold = models.CharField(max_length=50)
    slider_image = models.ImageField(upload_to='index/images/')
    def __str__(self):
        return f'{self.greetings}, {self.title_bold}'
    
class Address(models.Model):
    street = models.CharField(max_length=250)
    hnr = models.CharField(max_length=10)
    postcod = models.CharField(max_length=4)
    city = models.CharField(max_length=20)
    country = CountryField()
    def __str__(self):
        return f'{self.country}, {self.city},{self.postcod},{self.street},{self.hnr}'