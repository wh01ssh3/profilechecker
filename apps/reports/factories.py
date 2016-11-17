import factory

from .models import OneTimeReport, PeriodicReport
from ..schedule.factories import OneTimeTaskFactory, PeriodicTaskFactory


class ReportFactory(factory.DjangoModelFactory):
    """Base factory for report factories with post generation hook to add
    ``passed_rules`` when instance creation
    """

    @factory.post_generation
    def passed_rules(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for rule in extracted:
                self.passed_rules.add(rule)


class OneTimeReportFactory(ReportFactory):
    """Factory for ``OneTimeReport`` model"""
    task = factory.SubFactory(OneTimeTaskFactory)

    class Meta:
        model = OneTimeReport


class PeriodicReportFactory(ReportFactory):
    """Factory for ``PeriodicReport`` model"""
    task = factory.SubFactory(PeriodicTaskFactory)

    class Meta:
        model = PeriodicReport
