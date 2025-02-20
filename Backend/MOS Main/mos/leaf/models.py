from django.db import models

class SatellitePassage(models.Model):
    passage_id = models.CharField(max_length=100, unique=True)  # Unique identifier
    satellite_id = models.CharField(max_length=100)
    ground_station_id = models.CharField(max_length=100)
    max_elevation = models.FloatField()
    passage_status = models.CharField(max_length=50)
    keyhole_bypass = models.BooleanField()
    source = models.CharField(max_length=50)
    aos = models.DateTimeField()
    tca = models.DateTimeField()
    los = models.DateTimeField()
    passage_result_id = models.CharField(max_length=50)
    policy_type = models.CharField(max_length=50)
    bandwidth_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Passage {self.passage_id} ({self.satellite_id})"

class PassageBooking(models.Model):
    candidateID = models.CharField(max_length=255, unique=True)
    passageID = models.CharField(max_length=255, blank=True, null=True)
    AOS = models.DateTimeField()
    LOS = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.candidateID} - {self.passageID}"
