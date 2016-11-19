from django.test import TestCase

from ..factories import OneTimeReportFactory


class ReportTestCase(TestCase):
    """Test case for ``ReportModel``"""

    def setUp(self):
        self.report = OneTimeReportFactory()

    def test_str(self):
        """Test for ``__str__`` method"""
        self.assertEqual(str(self.report),
                         '{obj.modified} @ {obj.task}'.format(obj=self.report))
