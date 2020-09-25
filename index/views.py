from django.shortcuts import render
from .models import IndexSlider
from .models import Navigation_brand
from .models import Address
from resume.models import ResumeSection
from resume.models import SectionEntries
from resume.models import Languages
from portfolio.models import Project
from portfolio.models import Services
from django.core.mail import send_mail


def index(request):
    sliders = IndexSlider.objects.all()
    adresses = Address.objects.all()
    sections = ResumeSection.objects.all()
    entries_lang = Languages.objects.all()
    # =========== Entries for categories of Resume ================
    entries_edu = SectionEntries.objects.filter(
        category__contains="Education").order_by('-from_year')
    entries_exp = SectionEntries.objects.filter(
        category__contains="Expe").order_by('-from_year')

    entries_cert = SectionEntries.objects.filter(
        category__contains="Certificatoins")
    projects = Project.objects.all()

    # ==========Services ===================
    services = Services.objects.all().order_by('title')
    # ==================== End=====================
    return render(request,
                  'index/index.html',
                  {
                      'sliders': sliders, 'adresses': adresses, 'sections': sections,
                      'entries_edu': entries_edu, 'entries_exp': entries_exp, 'entries_lang': entries_lang,
                      'entries_cert': entries_cert, 'projects': projects, 'services': services
                  }
                  )


def contact(request):
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
        return render(request, 'index/contact.html', {'form_name': form_name})
    else:
        sliders = IndexSlider.objects.all()
        adresses = Address.objects.all()
        sections = ResumeSection.objects.all()
        entries_lang = Languages.objects.all()
        # =========== Entries for categories of Resume ================
        entries_edu = SectionEntries.objects.filter(
            category__contains="Education").order_by('-from_year')
        entries_exp = SectionEntries.objects.filter(
            category__contains="Expe").order_by('-from_year')

        entries_cert = SectionEntries.objects.filter(
            category__contains="Certificatoins")
        projects = Project.objects.all()

    # ==========Services ===================
        services = Services.objects.all().order_by('title')
    # ==================== End=====================
        return render(request,
                      'index/index.html',
                      {
                          'sliders': sliders, 'adresses': adresses, 'sections': sections,
                          'entries_edu': entries_edu, 'entries_exp': entries_exp, 'entries_lang': entries_lang,
                          'entries_cert': entries_cert, 'projects': projects, 'services': services
                      }
                      )
