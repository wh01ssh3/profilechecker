from django.db import models
from django_extensions.db.models import TimeStampedModel


class Report(TimeStampedModel):
    """Base class for reports

    Attributes:
        passed_rules (list[Rule]): Rules which checking is successful
    """

    passed_rules = models.ManyToManyField('rules.rule', blank=True)

    def __str__(self):
        return '{obj.modified} @ {obj.task}'.format(obj=self)

    class Meta:
        abstract = True


class OneTimeReport(Report):
    """Model for storing reports for one time tasks"""
    task = models.ForeignKey('schedule.OneTimeTask', related_name='reports')


class PeriodicReport(Report):
    """Model for storing reports for periodic tasks"""
    task = models.ForeignKey('schedule.PeriodicTask', related_name='reports')
