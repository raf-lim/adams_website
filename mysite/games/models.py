from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _
# from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from sorl.thumbnail import ImageField


class Chapter(models.Model):
    class Meta:
        verbose_name = _("chapter")
        verbose_name_plural = _("chapters")

    name = models.CharField(max_length=64, unique=True, verbose_name=_("name"))
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    name = models.CharField(max_length=64, unique=True, verbose_name=_("name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("games:category_detail", args=[self.pk])


class Game(models.Model):

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    name = models.CharField(max_length=255, unique=True, verbose_name=_("name"))
    description = models.TextField(default=None, null=True, blank=True, verbose_name=_("description"))
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    website = models.URLField(null=True, blank=True, verbose_name=_("website"))
    image = ImageField(upload_to="games/img/games/", blank=True, null=True)
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("games:game_detail", args=[self.pk])


class Character(models.Model):
    class Meta:
        verbose_name = _("character")
        verbose_name_plural = _("characters")

    name = models.CharField(max_length=255, unique=True, verbose_name=_("name"))
    description = models.TextField(default=None, null=True, blank=True, verbose_name=_("description"))
    image = ImageField(upload_to="games/img/characters/", null=True, blank=True)
    slug = AutoSlugField(populate_from="name")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True, related_name="characters")
    chapter = models.ForeignKey(Chapter, models.SET_NULL, null=True, blank=True, related_name="characters")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("games:character_detail", args=[self.pk])





