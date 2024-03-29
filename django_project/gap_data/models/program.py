"""Program model."""
from django.contrib.gis.db import models

from core.models import SlugTerm, IconTerm
from gap_data.models.instance import Instance
from gap_data.models.scenario import ScenarioLevel


class Program(SlugTerm, IconTerm):
    """Program model."""

    pass


class ProgramInstance(models.Model):
    """Program model linked to an instance."""

    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE
    )
    instance = models.ForeignKey(
        Instance,
        on_delete=models.CASCADE
    )

    class Meta:  # noqa: D106
        unique_together = ('program', 'instance')


class ProgramIntervention(models.Model):
    """Intervention of program model."""

    program_instance = models.ForeignKey(
        ProgramInstance,
        on_delete=models.CASCADE
    )
    scenario_level = models.ForeignKey(
        ScenarioLevel,
        on_delete=models.CASCADE
    )
    intervention_url = models.TextField()

    class Meta:  # noqa: D106
        unique_together = ('program_instance', 'scenario_level')
