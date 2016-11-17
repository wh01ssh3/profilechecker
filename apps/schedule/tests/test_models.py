from django.test import SimpleTestCase

from ..factories import OneTimeTaskFactory


class OneTimeTaskTestCase(SimpleTestCase):
    """Test case for ``OneTimeTask`` model"""

    def setUp(self):
        self.task = OneTimeTaskFactory.build()

    def test_str(self):
        """Test ``__str__`` method"""
        self.assertEqual(str(self.task),
                         '{obj.user} @ {obj.time}'.format(obj=self.task))
