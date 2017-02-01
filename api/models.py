import datetime
from django.db import models

from .utils import item_upload_to


class Mixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_created_display(self):
        return get_time_display(self.created)

    def get_modified_display(self):
        return get_time_display(self.modified)


class FoodGroup(Mixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __unicode__(self):
        return 'FoodGroup(%s)' % self.slug

class Food(Mixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to=item_upload_to, null=True, blank=True)
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    food_group = models.ForeignKey('FoodGroup', related_name="food_groups", null=True, blank=True)
    place = models.ForeignKey('Place', related_name="food_place", null=True, blank=True)

    def __unicode__(self):
        return 'Food(%s)' % self.slug


class Place(Mixin):
    RESTAURANT = 'restaurant'
    PAVEMENT = 'pavement'
    PLACE_TYPE_CHOICES = (
        (RESTAURANT, 'Restaurant'),
        (PAVEMENT, 'Pavement'),
    )

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to=item_upload_to, null=True, blank=True)
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    location =  models.CharField(max_length=255, null=True, blank=True)
    place_type = models.CharField(max_length=100, choices=PLACE_TYPE_CHOICES)

    def __unicode__(self):
        return 'Place #%s' % self.id
