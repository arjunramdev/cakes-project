from django.contrib import admin

# Register your models here.

from .import models

admin.site.register(models.Cake)

admin.site.register(models.Category)

admin.site.register(models.Shape)

admin.site.register(models.Weight)