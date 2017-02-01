from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer, FoodSerializer, PlaceSerializer, FoodGroupSerializer
from .models import Food, Place, FoodGroup


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = Food.objects.all()
        food_group = self.request.query_params.get('food_group', None)
        if food_group is not None:
            queryset = queryset.filter(food_group__slug=food_group)

        place = self.request.query_params.get('place', None)
        if place is not None:
            queryset = queryset.filter(place__slug=place)

        return queryset



class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class FoodGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FoodGroup.objects.all()
    serializer_class = FoodGroupSerializer
