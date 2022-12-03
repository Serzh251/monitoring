from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models


class DataTransport(models.Model):
    dut1 = models.FloatField(max_length=10000, blank=True, null=True)
    dut2 = models.FloatField(max_length=10000, blank=True, null=True)
    dut3 = models.FloatField(max_length=10000, blank=True, null=True)
    dut4 = models.FloatField(max_length=10000, blank=True, null=True)
    engine_left = models.CharField(max_length=300, blank=True, null=True)
    engine_right = models.CharField(max_length=300, blank=True, null=True)
    engine_aux1 = models.CharField(max_length=300, blank=True, null=True)
    engine_aux2 = models.CharField(max_length=300, blank=True, null=True)
    energy_params = models.CharField(max_length=300, blank=True, null=True)
    params = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.dut1} | {self.dut2}'


class Trip(models.Model):
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='start time')
    stop_time = models.DateTimeField(verbose_name='stop time', blank=True, null=True)
    distance = models.FloatField(verbose_name='distance trip', blank=True, null=True)
    geom = models.LineStringField(verbose_name='trip track', blank=True, null=True)

    def __str__(self):
        return f'{self.start_time.strftime("%H:%M %d.%m.%Y")} | {self.stop_time.strftime("%H:%M %d.%m.%Y")} | ' \
               f'{self.distance}'


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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='owner', related_name='owner')
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default='SHIP', verbose_name='type')
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='STOP', verbose_name='state')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='trip', blank=True, null=True)
    data = models.ForeignKey(DataTransport, on_delete=models.CASCADE, verbose_name='data transport',
                             blank=True, null=True)

    def __str__(self):
        return self.name


class DataCoordinates(models.Model):
    class Meta:
        ordering = ['-add_datetime']

    geom = models.PointField(srid=4326)
    add_datetime = models.DateTimeField(verbose_name='time to add', auto_now_add=True, blank=True, null=True)
    transport = models.ForeignKey(Transport, on_delete=models.PROTECT, blank=True, null=True, related_name='transport')
    data_for_points = models.ForeignKey(DataTransport, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='data_for_points')
    velocity = models.FloatField(verbose_name='velocity', blank=True, null=True)
    course = models.FloatField(verbose_name='course', blank=True, null=True)

    def __str__(self):
        return f'{self.add_datetime.strftime("%H:%M %d.%m.%Y")} | {self.geom} | {self.transport}'

    @property
    def transport_name(self):
        if self.transport:
            return self.transport.name
        return ''

    @property
    def transport_velocity(self):
        if self.velocity:
            return self.velocity
        return ''
