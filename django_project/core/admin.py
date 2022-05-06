"""Core admin."""
from django.conf import settings
from django.contrib import admin

from core.models import SitePreferences

admin.site.register(SitePreferences, admin.ModelAdmin)
admin.site.site_url = settings.DJANGO_HOME_URL
