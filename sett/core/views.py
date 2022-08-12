from django.shortcuts import render
from .models import PortfolioItem, Certificates, Experiencia


def home(request):
    pfi = PortfolioItem.objects.all().order_by('-create_at')
    cert = Certificates.objects.all().order_by('-create_at')
    exp = Experiencia.objects.all().order_by('-create_at')

    context = {'pfi': pfi, 'cert': cert, 'exp': exp}

    return render(request, 'home.html', context)