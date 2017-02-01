from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Food, Place, FoodGroup


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    place_type = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('name', 'description', 'photo', 'slug', 'location', 'place_type')

    def get_place_type(self,obj):
        return obj.get_place_type_display()


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    food_group = serializers.SlugRelatedField(
        read_only=True,
        slug_field='slug'
     )

    place = PlaceSerializer()

    class Meta:
        model = Food
        fields = ('name', 'description', 'photo', 'slug', 'food_group', 'place')


class FoodGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodGroup
        fields = ('name', 'slug')
