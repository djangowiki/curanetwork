from rest_framework import serializers
from .models import Property, Booking


class PropertyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name']


class BookingModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id', 'name', 'price', 'property']

