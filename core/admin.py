from django.contrib import admin
from .models import Certificates, Experiencia, PortfolioItem


admin.site.register(PortfolioItem)
admin.site.register(Certificates)
admin.site.register(Experiencia)