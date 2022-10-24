from django.db import models
from cloudinary.models import CloudinaryField

# Modulos para borrar la imagen que se sube a cloudinary
import cloudinary
import cloudinary.uploader
from django.dispatch import receiver
from django.db.models.signals import pre_delete

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = CloudinaryField('image', folder='portfolio-personal/proyectos')
    github = models.URLField(max_length=200, blank=True)
    url = models.URLField(max_length=200, blank=True)
    blog = models.URLField(max_length=200, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=PortfolioItem)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)


class Certificates(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    image = CloudinaryField('image', folder='portfolio-personal/certificados')
    alt_image = models.CharField(max_length=250)
    link_cert = models.URLField(max_length=200, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Certificate'

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Certificates)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)


class Experiencia(models.Model):
    año = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Experiencia'