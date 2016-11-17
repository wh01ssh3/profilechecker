import factory
import pytz
from django.conf import settings

from .models import OneTimeTask, PeriodicTask


class UserFactory(factory.DjangoModelFactory):
    """Factory for ``User`` model"""

    username = factory.Faker('name')

    class Meta:
        model = settings.AUTH_USER_MODEL


class TaskFactory(factory.DjangoModelFactory):
    """Base factory for task types"""
    title = factory.Faker('catch_phrase')
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def rules(self, create, extracted, **kwargs):
        """Generate Many-To-Many ``Task`` -> ``Rule`` relationship"""
        if not create:
            return
        if extracted:
            for rule in extracted:
                self.rules.add(rule)

    @factory.post_generation
    def profiles(self, create, extracted, **kwargs):
        """Generate Many-To-Many ``Task`` -> ``Profile`` relationship"""
        if not create:
            return
        if extracted:
            for profile in extracted:
                self.profiles.add(profile)


class OneTimeTaskFactory(TaskFactory):
    """Factory for ``OneTimeTask`` model"""
    time = factory.Faker('date_time', tzinfo=pytz.utc)

    class Meta:
        model = OneTimeTask


class PeriodicTaskFactory(TaskFactory):
    """Factory for ``PeriodicTask`` model"""

    class Meta:
        model = PeriodicTask
