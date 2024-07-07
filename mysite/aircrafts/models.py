from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _
# from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from sorl.thumbnail import ImageField


class Manufacturer(models.Model):
    class Meta:
        verbose_name = _("manufacturer")
        verbose_name_plural = _("manufacturers")

    name = models.CharField(max_length=64, unique=True, verbose_name=_("name"))
    website = models.URLField(null=True, blank=True, verbose_name=_("website"))
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return f"{self.name}"


class EngineCategory(models.Model):
    class Meta:
        verbose_name = _("engine category")
        verbose_name_plural = _("engine categories")

    name = models.CharField(max_length=64, unique=True, verbose_name=_("name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("aircrafts:engine_category_detail", args=[self.pk])


class Aircraft(models.Model):

    class Meta:
        verbose_name = _("Aircraft")
        verbose_name_plural = _("Aircrafts")

    name = models.CharField(max_length=255, unique=True, verbose_name=_("name"))
    description = models.TextField(default=None, null=True, blank=True, verbose_name=_("description"))
    engine_category = models.ForeignKey(EngineCategory, models.SET_NULL, null=True, blank=True)
    website = models.URLField(null=True, blank=True, verbose_name=_("website"))
    image = ImageField(upload_to="aircrafts/img/aircrafts/", blank=True, null=True)
    slug = AutoSlugField(populate_from="name")
    manufacturer = models.ForeignKey(Manufacturer, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("aircrafts:aircraft_detail", args=[self.pk])
