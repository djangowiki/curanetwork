from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
    long = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Properties'


class Booking(models.Model):
    name = models.CharField(max_length=100)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
