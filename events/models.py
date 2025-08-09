from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class EventType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    # attendance_count = models.JSONField(default=dict)  # Stores {'total': 0, 'members': 0, 'visitors': 0}
    
    sermon = models.TextField(blank=True, null=True)
    # status = models.CharField(max_length=10, choices=EVENT_STATUS_CHOICES, default='Active')
    stream_url = models.URLField(help_text="YouTube Live URL", blank=True, null=True)
    is_live = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
