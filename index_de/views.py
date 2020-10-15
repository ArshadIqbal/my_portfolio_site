from django.shortcuts import render
from .models import IndexSlider_de
from .models import Navigation_brand_de
from .models import Address_de
from .models import ResumeSection_de
from .models import SectionEntries_de
from .models import Languages_de
from .models import Project_de
from .models import Services_de

from django.core.mail import send_mail


def index_de(request):
    sliders = IndexSlider_de.objects.all()
    adresses = Address_de.objects.all()
    sections = ResumeSection_de.objects.all()
    entries_lang = Languages_de.objects.all()
    # =========== Entries for categories of Resume ================
    entries_edu = SectionEntries_de.objects.filter(
        category__contains="Ausbildung").order_by('-from_year')
    entries_exp = SectionEntries_de.objects.filter(
        category__contains="Beruf").order_by('-from_year')

    entries_cert = SectionEntries_de.objects.filter(
        category__contains="Zertifikate")
    projects = Project_de.objects.all()

    # ==========Services ===================
    services = Services_de.objects.all().order_by('title')
    # ==================== End=====================
    return render(request,
                  'index_de/index_de.html',
                  {
                      'sliders': sliders, 'adresses': adresses, 'sections': sections,
                      'entries_edu': entries_edu, 'entries_exp': entries_exp, 'entries_lang': entries_lang,
                      'entries_cert': entries_cert, 'projects': projects, 'services': services
                  }
                  )


def contact_de(request):
    if request.method == "POST":
        form_name = request.POST['form-name']
        form_email = request.POST['form-email']
        form_Subject = request.POST['form-Subject']
        form_text = request.POST['form-text']

        send_mail(
            form_Subject,  # subject
            form_text,  # message
            form_email,  # from email
            ['admin@arshadiqbal.com'],
            # to email
        )
        return render(request, 'index_de/contact_de.html', {'form_name': form_name})
    else:
        sliders = IndexSlider_de.objects.all()
        adresses = Address_de.objects.all()
        sections = ResumeSection_de.objects.all()
        entries_lang = Languages_de.objects.all()
        # =========== Entries for categories of Resume ================
        entries_edu = SectionEntries_de.objects.filter(
            category__contains="Ausbildung").order_by('-from_year')
        entries_exp = SectionEntries_de.objects.filter(
            category__contains="Berufs").order_by('-from_year')

        entries_cert = SectionEntries_de.objects.filter(
            category__contains="Zertifikate")
        projects = Project_de.objects.all()

    # ==========Services ===================
        services = Services_de.objects.all().order_by('title')
    # ==================== End=====================
        return render(request,
                      'index/index.html',
                      {
                          'sliders': sliders, 'adresses': adresses, 'sections': sections,
                          'entries_edu': entries_edu, 'entries_exp': entries_exp, 'entries_lang': entries_lang,
                          'entries_cert': entries_cert, 'projects': projects, 'services': services
                      }
                      )
