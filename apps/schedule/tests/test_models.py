from django.test import SimpleTestCase, TestCase

from apps.rules.factories import ProfileFactory, RuleFactory
from apps.schedule.factories import PeriodicTaskFactory
from ..factories import OneTimeTaskFactory


class OneTimeTaskTestCase(TestCase):
    """Test case for ``OneTimeTask`` model"""

    def setUp(self):
        self.rules = RuleFactory.create_batch(3)

        # Main profile contains all rules
        self.main_profile = ProfileFactory(rules=self.rules)

        # Profile with 2 rules
        self.profile = ProfileFactory(rules=self.rules[0:2])

        # Task with main profile
        self.main_task = OneTimeTaskFactory(profiles=[self.main_profile])

        # Task with profile
        self.task = OneTimeTaskFactory(profiles=[self.profile],
                                       rules=[self.rules[-1]])

        # Task with crossing
        self.task_crossing = OneTimeTaskFactory(profiles=[self.profile],
                                                rules=self.rules[1:3])

    def test_str(self):
        """Test ``__str__`` method"""
        self.assertEqual(str(self.main_task),
                         '{obj.user} @ {obj.time}'.format(obj=self.main_task))

    def test_get_all_rules_main_profile(self):
        """Ensure that ``get_all_rules`` returns all rules of profile"""
        self.assertEqual(self.main_task.get_all_rules().count(),
                         len(self.rules))

    def test_get_all_rules_union(self):
        """Ensure that ``get_all_rules`` when we have profile with 2 rules and
        rule which doesn't contain in profile, returns all set of rules
        """
        self.assertEqual(self.task.get_all_rules().count(), len(self.rules))

    def test_get_all_rules_crossing(self):
        """Ensure that ``get_all_rules`` removes crossing elements from
        resulting queryset
        """
        self.assertEqual(self.task_crossing.get_all_rules().count(),
                         len(self.rules))


class PeriodicTaskTestCase(SimpleTestCase):
    """Test case for ``PeriodicTask``"""

    def setUp(self):
        self.task = PeriodicTaskFactory.build()

    def test_str(self):
        """Ensure that periodic task ``__str__`` method returns ``title``
        attribute
        """
        self.assertEqual(str(self.task), self.task.title)
