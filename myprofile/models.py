from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile)
    member_name = models.CharField(max_length=100)
    relationship_name = models.CharField(max_length=100)
