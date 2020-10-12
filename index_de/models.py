from django.db import models
from django_countries.fields import CountryField
import datetime


class IndexSlider_de(models.Model):
    greetings = models.CharField(max_length=50)
    title_bold = models.CharField(max_length=50)
    slider_image = models.ImageField(upload_to='index/images/')

    def __str__(self):
        return f'{self.greetings}, {self.title_bold}'


class Address_de(models.Model):
    street = models.CharField(max_length=250)
    hnr = models.CharField(max_length=10)
    postcod = models.CharField(max_length=4)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.city},{self.postcod},{self.street},{self.hnr}'


class Navigation_brand_de(models.Model):
    nav_brand = models.CharField(max_length=50)
    nav_image = models.ImageField(upload_to='index/images/')

    def __str__(self):
        return f'{self.nav_brand}'


# Create your models here.
section_category_de = (
    ('Berufslaufbahn', 'Berufslaufbahn'),
    ('Ausbildung', 'Ausbildung'),
    ('Zertifikate', 'Zertifikate'),
    ('Sprachen', 'Sprachen')
)


class ResumeSection_de(models.Model):
    section = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='myresume/images/', blank=True, null=True)
#    section = models.ForeignKey(SectionEntry, on_delete=models.CASCADE)
    url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.section}'


class SectionEntries_de(models.Model):

    category = models.CharField(
        max_length=25, choices=section_category_de, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    institution_url = models.URLField(blank=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    company_url = models.URLField(blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(null=True, default='Austria')

    #    from_year   = models.IntegerField(validators=[MinValueValidator(1988), MaxValueValidator(current_year)])
    from_year = models.DateField(default=None, blank=True, null=True)
    is_current = models.BooleanField(default=False)
    to_year = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.category},{self.title},{self.institution},{self.company},{self.city},{self.country}'


class Languages_de(models.Model):
    name = models.CharField(max_length=20)
    lang_flag = models.ImageField(
        upload_to='myresume/images/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Project_de(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(
        upload_to='portfolio/images/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.title},{self.url}'


class Services_de(models.Model):
    title = models.CharField(max_length=15)
    fa_url = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'
