from django.urls import path, include
from rest_framework import routers
from .views import PropertyViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register('bookings', BookingViewSet)
router.register('properties', PropertyViewSet)
urlpatterns = [
    path('', include(router.urls)),
]