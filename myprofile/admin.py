from django.contrib import admin

from .models import Profile, FamilyMember

admin.site.register(Profile)
admin.site.register(FamilyMember)