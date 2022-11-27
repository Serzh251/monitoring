from django.db import models
from django.contrib.auth.models import User
# from djgeojson.fields import PointField


class DataTransport(models.Model):
    pass


class DataCoordinates(models.Model):
#     geom = PointField(blank=True, null=True)
    pass


class Trip(models.Model):
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='start time')
    stop_time = models.DateTimeField(verbose_name='stop time', blank=True, null=True)
    distance = models.FloatField(verbose_name='distance trip', blank=True, null=True)
    geo_data = models.ForeignKey(DataCoordinates, on_delete=models.CASCADE, verbose_name='data trip')


class Transport(models.Model):
    TYPE_CHOICES = [
        ('SHIP', 'ship'),
        ('CAR', 'car'),
    ]

    STATE_CHOICES = [
        ('STOP', 'stop'),
        ('MOVE', 'move'),
        ('NO CONNECTION', 'no connection'),
    ]

    name = models.CharField(max_length=200, verbose_name='name')
    description = models.CharField(max_length=300, verbose_name='description', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='owner')
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default='SHIP', verbose_name='type')
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='STOP', verbose_name='state')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='trip', blank=True, null=True)
    data = models.ForeignKey(DataTransport, on_delete=models.CASCADE, verbose_name='data transport',
                             blank=True, null=True)

    def __str__(self):
        return self.name

