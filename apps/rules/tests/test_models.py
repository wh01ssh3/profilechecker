from django.test import SimpleTestCase

from ..factories import RuleFactory, ProfileFactory


class RuleTestCase(SimpleTestCase):
    """Test case for ``Rule`` model"""

    def setUp(self):
        self.rule = RuleFactory.build()

    def test_str(self):
        """Test ``__str__`` method"""
        self.assertEqual(str(self.rule), self.rule.title)


class ProfileTestCase(SimpleTestCase):
    """Test case for ``Profile`` model"""

    def setUp(self):
        self.profile = ProfileFactory.build()

    def test_str(self):
        """Test ``__str__`` method"""
        self.assertEqual(str(self.profile), self.profile.title)
