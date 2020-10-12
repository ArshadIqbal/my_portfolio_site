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

from index_de.models import IndexSlider_de, Address_de, Navigation_brand_de, ResumeSection_de, SectionEntries_de, Languages_de, Project_de, Services_de

admin.site.register(IndexSlider)
admin.site.register(Address)
admin.site.register(Navigation_brand)
admin.site.register(ResumeSection)
admin.site.register(SectionEntries)
admin.site.register(Languages)
admin.site.register(Project)
admin.site.register(Services)
admin.site.register(NewArrivals)

admin.site.register(IndexSlider_de)
admin.site.register(Address_de)
admin.site.register(Navigation_brand_de)
admin.site.register(ResumeSection_de)
admin.site.register(SectionEntries_de)
admin.site.register(Languages_de)
admin.site.register(Project_de)
admin.site.register(Services_de)
