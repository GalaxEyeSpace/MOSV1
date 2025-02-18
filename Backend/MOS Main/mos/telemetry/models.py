from django.db import models

class Velocity(models.Model):
    timestamp = models.DateTimeField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def __str__(self):
        return f"Velocity at {self.timestamp}"

class Storage(models.Model):
    timestamp = models.DateTimeField()
    instant_data_gen = models.IntegerField()
    instant_data_down = models.IntegerField()
    ssd_storage = models.IntegerField()
    ssd_capacity = models.IntegerField()

    def __str__(self):
        return f"Storage at {self.timestamp}"

class Power(models.Model):
    timestamp = models.DateTimeField()
    net_power = models.FloatField()
    solar = models.FloatField()
    storage = models.FloatField()

    def __str__(self):
        return f"Power at {self.timestamp}"

class Position(models.Model):
    timestamp = models.DateTimeField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def __str__(self):
        return f"Position at {self.timestamp}"