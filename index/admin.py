from django.contrib import admin
from .models import IndexSlider
from .models import Address
from .models import Navigation_brand
from resume.models import ResumeSection
from resume.models import SectionEntries
from resume.models import Languages
from portfolio.models import Project
from portfolio.models import Services
from chotihatti.models import NewArrivals


admin.site.register(IndexSlider)
admin.site.register(Address)
admin.site.register(Navigation_brand)
admin.site.register(ResumeSection)
admin.site.register(SectionEntries)
admin.site.register(Languages)
admin.site.register(Project)
admin.site.register(Services)
admin.site.register(NewArrivals)
