from django.contrib.admin import AdminSite
from django.test import TestCase

from ..admin import OneTimeTaskAdmin
from ..factories import OneTimeTaskFactory
from ..models import OneTimeTask
from ...rules.factories import RuleFactory, ProfileFactory


class TaskAdminTest(TestCase):
    """Test case for ``OneTimeTaskAdmin`` and ``PeriodicTaskAdmin`` classes"""

    def setUp(self):
        self.admin = OneTimeTaskAdmin(OneTimeTask, AdminSite())
        self.task = OneTimeTaskFactory(rules=[RuleFactory()],
                                       profiles=[ProfileFactory()])

    def test_rules_count(self):
        """Test ``rules_count`` admin method"""
        self.assertEqual(self.admin.rules_count(self.task),
                         self.task.rules.count())

    def test_profiles_count(self):
        """Test ``profiles_count`` admin method"""
        self.assertEqual(self.admin.profiles_count(self.task),
                         self.task.profiles.count())
