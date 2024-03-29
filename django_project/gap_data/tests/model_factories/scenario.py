"""Factory for ScenarioLevel."""
import factory

from gap_data.models.scenario import ScenarioLevel
from gap_data.tests.model_factories.instance import InstanceF


class ScenarioLevelF(factory.django.DjangoModelFactory):
    """Factory for ScenarioLevel."""

    instance = factory.SubFactory(InstanceF)
    name = factory.Sequence(lambda n: 'Scenario Level {}'.format(n))
    level = factory.Sequence(lambda n: n)

    class Meta:  # noqa: D106
        model = ScenarioLevel
