from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Anomaly(models.Model):
    location = models.CharField(max_length=255, blank=True, null=True)
    camera_id = models.CharField(max_length=50, blank=True, null=True)
    ipaddress = models.CharField(max_length=45, blank=True, null=True)
    anomaly_code = models.CharField(max_length=50, blank=True, null=True)
    anomaly_name = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.FloatField(blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    actions_taken = models.TextField(blank=True, null=True)
    videopath = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'anomalies'


class AlarmHistory(models.Model):
    room = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    activated_by = models.CharField(max_length=150)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'alarm_history'
