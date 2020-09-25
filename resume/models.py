from django.db import models
from django_countries.fields import CountryField
import datetime

# Create your models here.

section_category = (
        ('Experience','Experience'),
        ('Education','Education'),
        ('Certificatoins','Certifications'),
        ('Languages','Languages')
    )
class ResumeSection(models.Model):
    section = models.CharField(max_length=100)
    image       = models.ImageField(upload_to='myresume/images/', blank=True, null=True)
#    section = models.ForeignKey(SectionEntry, on_delete=models.CASCADE)
    url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.section}'

class SectionEntries(models.Model):
    
    category = models.CharField(max_length=25, choices=section_category, blank=True, null=True)
    title       = models.CharField(max_length=100)
    description     = models.TextField(max_length=500, blank=True, null=True)
    institution       = models.CharField(max_length=100,blank=True, null=True)
    institution_url = models.URLField(blank=True)
    company = models.CharField(max_length=100,blank=True, null=True)
    company_url = models.URLField(blank=True)
    city = models.CharField(max_length=100, blank=True,null=True)
    country = CountryField(null=True,default='Austria')

    #    from_year   = models.IntegerField(validators=[MinValueValidator(1988), MaxValueValidator(current_year)])
    from_year = models.DateField(default=None, blank=True, null=True)
    is_current  = models.BooleanField(default=False)
    to_year     = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.category},{self.title},{self.institution},{self.company},{self.city},{self.country}'

class Languages(models.Model):
    name = models.CharField(max_length=20)
    lang_flag = models.ImageField(upload_to='myresume/images/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'