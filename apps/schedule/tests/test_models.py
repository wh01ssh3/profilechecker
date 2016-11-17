from django.test import SimpleTestCase

from apps.schedule.factories import PeriodicTaskFactory
from ..factories import OneTimeTaskFactory


class OneTimeTaskTestCase(SimpleTestCase):
    """Test case for ``OneTimeTask`` model"""

    def setUp(self):
        self.task = OneTimeTaskFactory.build()

    def test_str(self):
        """Test ``__str__`` method"""
        self.assertEqual(str(self.task),
                         '{obj.user} @ {obj.time}'.format(obj=self.task))


class PeriodicTaskTestCase(SimpleTestCase):
    """Test case for ``PeriodicTask``"""

    def setUp(self):
        self.task = PeriodicTaskFactory()

    def test_str(self):
        """Ensure that periodic task ``__str__`` method returns ``title``
        attribute
        """
        self.assertEqual(str(self.task), self.task.title)
