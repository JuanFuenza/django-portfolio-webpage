from django.shortcuts import render
from .models import PortfolioItem, Certificates, Experiencia


def home(request):
    pfi = PortfolioItem.objects.all()
    cert = Certificates.objects.all()
    exp = Experiencia.objects.all()

    context = {'pfi': pfi, 'cert': cert, 'exp': exp}

    return render(request, 'home.html', context)