from django.db import models
from django.urls import reverse
from django.utils import timezone


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)

    def __str__(self):
        return self.name
