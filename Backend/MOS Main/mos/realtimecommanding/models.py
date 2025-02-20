from django.db import models

class UplinkMessage(models.Model):
    payload = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"UplinkMessage at {self.timestamp}"

class DownlinkMessage(models.Model):
    payload = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DownlinkMessage at {self.timestamp}"