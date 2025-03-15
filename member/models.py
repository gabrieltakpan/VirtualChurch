# user_management/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    TITLE_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
        ('Rev', 'Rev'),
    ]
    title = models.CharField(max_length=5, choices=TITLE_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


class Family(models.Model):
    family_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=15, blank=True, null=True)
    wedding_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.family_name

class FamilyMember(models.Model):
    FAMILY_ROLES = [
        ('Husband', 'Husband'),
        ('Wife', 'Wife'),
        ('Child', 'Child'),
        ('Other Relative', 'Other Relative'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, related_name='members', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=FAMILY_ROLES)
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    birth_year = models.IntegerField()
    classification = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.role}'
