from django.db import models
from django_extensions.db.models import TimeStampedModel


class Report(TimeStampedModel):
    """Base class for reports"""

    def __str__(self):
        return '{obj.modified} @ {obj.task}'.format(obj=self)

    class Meta:
        abstract = True


class OneTimeReport(Report):
    """Model for storing reports for one time tasks

    Attributes:
        passed_rules (list[Rule]): Rules which checking is successful
        total_rules (list[Rule]): Rules which should be checked total
    """
    passed_rules = models.ManyToManyField(
        'rules.rule',
        blank=True,
        related_name='one_time_reports_where_passed'
    )
    total_rules = models.ManyToManyField(
        'rules.rule',
        blank=True,
        related_name='one_time_reports_where_total'
    )
    task = models.ForeignKey('schedule.OneTimeTask', related_name='reports')


class PeriodicReport(Report):
    """Model for storing reports for periodic tasks

    Attributes:
        passed_rules (list[Rule]): Rules which checking is successful
        total_rules (list[Rule]): Rules which should be checked total
    """
    passed_rules = models.ManyToManyField(
        'rules.rule',
        blank=True,
        related_name='periodic_reports_where_passed'
    )
    total_rules = models.ManyToManyField(
        'rules.rule',
        blank=True,
        related_name='periodic_reports_where_total'
    )
    task = models.ForeignKey('schedule.PeriodicTask', related_name='reports')
