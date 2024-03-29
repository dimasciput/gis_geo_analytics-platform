"""Model for Website Preferences."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models.singleton import SingletonModel


class SitePreferences(SingletonModel):
    """Preference settings specifically for website.

    Preference contains
    - site_title
    - primary_color
    - secondary_color
    - icon
    -favicon
    """

    site_title = models.CharField(
        max_length=512,
        default=''
    )
    primary_color = models.CharField(
        max_length=16,
        null=True, blank=True,
        default='#1CABE2',
        help_text=_(
            'Put the hex color with # (e.g. #ffffff) '
            'or put the text of color. (e.g. blue)')
    )
    secondary_color = models.CharField(
        max_length=16,
        null=True, blank=True,
        default='#E34E09',
        help_text=_(
            'Put the hex color with # (e.g. #ffffff) '
            'or put the text of color. (e.g. blue)')
    )
    icon = models.FileField(
        upload_to='settings/icons',
        null=True,
        blank=True
    )
    favicon = models.FileField(
        upload_to='settings/icons',
        null=True,
        blank=True
    )

    class Meta:  # noqa: D106
        verbose_name_plural = "site preferences"

    @staticmethod
    def preferences() -> "SitePreferences":
        """Load Site Preference."""
        return SitePreferences.load()

    def __str__(self):
        return 'Site Preference'
