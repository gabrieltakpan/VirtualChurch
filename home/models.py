from django.db import models
from django.contrib.auth.models import User
import urllib.parse 

class LiveStream(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stream_url = models.URLField(help_text="YouTube Live URL")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Sermon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(help_text="YouTube or Azure Video URL")
    scripture = models.TextField()
    scripture_link = models.URLField(blank=True, null=True, help_text="Link to Bible Gateway search")
    notes = models.TextField()
    questions = models.TextField()
    image = models.ImageField(upload_to='sermon_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.scripture:
            # Split the scripture references into lines
            scripture_lines = self.scripture.split("\n")  # Splitting by newline
            first_scripture = scripture_lines[0].strip() if scripture_lines else ""  # Get the first line
            
            base_url = "https://www.bible.com/search/bible?query="
            encoded_scripture = urllib.parse.quote(first_scripture)  # Encode first scripture line
            self.scripture_link = base_url + encoded_scripture  # Save only the first scripture link
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - ${self.amount}"

# Community Resources (Bible Study, Events, Forums)
class Resource(models.Model):
    RESOURCE_TYPES = (
        ('bible_study', 'Bible Study'),
        ('event', 'Event'),
        ('forum', 'Forum Discussion'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    resource_type = models.CharField(max_length=15, choices=RESOURCE_TYPES)
    files = models.FileField(upload_to='learning_files', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_resource_type_display()}: {self.title}"

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.title} - {self.date}"

