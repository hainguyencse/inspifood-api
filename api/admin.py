from django.contrib import admin

from .models import Food, Place, FoodGroup

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'photo', 'slug']
    search_fields = ('name', 'slug')


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'photo', 'slug', 'location', 'place_type']
    search_fields = ('name', 'slug', 'place_type')


class FoodGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ('name', 'slug')


admin.site.register(Food, FoodAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(FoodGroup, FoodGroupAdmin)
