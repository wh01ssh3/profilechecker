import factory

from .models import Profile, Rule


class RuleFactory(factory.DjangoModelFactory):
    """Factory for ``Rule`` model"""

    title = factory.Faker('catch_phrase')
    code = factory.Faker('text')

    class Meta:
        model = Rule


class ProfileFactory(factory.DjangoModelFactory):
    """Factory for ``Profile`` model"""

    title = factory.Faker('catch_phrase')

    @factory.post_generation
    def rules(self, create, extracted, **kwargs):
        """Create rules.

        Post-generation hook to create relations for rules which should be
        included in profile.
        """
        if not create:
            return
        if extracted:
            for rule in extracted:
                self.rules.add(rule)

    class Meta:
        model = Profile
