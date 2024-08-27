from django.db import models
from django.utils.text import slugify

class Cartochka(models.Model):
  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250,unique=True, blank=True)
  description = models.TextField(max_length=500)


