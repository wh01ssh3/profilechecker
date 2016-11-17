from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

from ..rules.models import Rule

TIME_METRIC_CHOICES = (
    ('s', 'seconds'),
    ('m', 'minutes'),
    ('h', 'hours'),
    ('d', 'days'),
    ('w', 'weeks'),
    ('M', 'months'),
    ('y', 'years')
)


class Task(TitleDescriptionModel):
    """Base model for storing tasks

    Tasks can have 2 kind of types: one-time and periodic. This model should
    allow to provide the same set of fields for these types of tasks.

    Attributes:
        user (User): User on which machine task will be executed
        rules (list[Rule]): Rules, which included into this task
        profiles (list[Profile]): Profiles, which included into task
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    rules = models.ManyToManyField('rules.rule', blank=True)
    profiles = models.ManyToManyField('rules.profile', blank=True)

    def get_all_rules(self):
        """Get rules from rules and profiles"""
        rules = Rule.objects.none()
        for profile in self.profiles.prefetch_related('rules'):
            rules |= profile.rules.all()

        rules |= self.rules.all()

        return rules

    class Meta:
        abstract = True


class OneTimeTask(Task):
    """Model for storing one shot tasks

    These tasks will be shot on the client machines only in one time

    Attributes:
        time (DateTime): Date and time when task should be executed
    """
    # To make this attribute non-require
    title = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField()

    def __str__(self):
        return '{obj.user} @ {obj.time}'.format(obj=self)


class PeriodicTask(TimeStampedModel, Task):
    """Model for storing periodic tasks

    These tasks also should be added in general set of tasks when client
    requests, all tasks which it should executes in near time.
    """

    every = models.PositiveIntegerField(default=1)
    metric = models.CharField(choices=TIME_METRIC_CHOICES, max_length=255,
                              default='h')

    def __str__(self):
        return self.title
