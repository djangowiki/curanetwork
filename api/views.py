from rest_framework import viewsets, status
from rest_framework.decorators import action

from .serializers import PropertyModelSerializer, BookingModelSerializer
from .models import Property, Booking
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

import requests
import json


# Property Viewset
class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyModelSerializer
    queryset = Property.objects.all()
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['GET', 'POST'])
    def bookings(self, request, pk='None'):
        # Fetch Bookings from the Database by Property
        booking = Booking.objects.select_related().all()
        serializer = BookingModelSerializer(booking, many=True)
        response = {'message': 'Property Bookings', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


# Bookings Viewset
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingModelSerializer
    queryset = Booking.objects.all()
    permission_classes = (AllowAny,)  # Application API is open at the moment.


def location(self, request):
    api_service_call = requests.get('https://places.ls.hereapi.com/places/v1/autosuggest?at=40.74917,'
                                    '-73.98529&q=chrysler&apiKey=lCd5ubBwiQhPFnb06L9CxybSfoOkRQQdLQWO_6KVfnA')
    api_parser = json.loads(api_service_call.content)
    response = {'api Data': api_parser}
    return Response(response, status.HTTP_200_OK)
