from django.contrib.admin import AdminSite
from django.test import TestCase

from ..admin import ReportAdmin
from ..factories import OneTimeReportFactory
from ..models import Report
from ...rules.factories import RuleFactory
from ...schedule.factories import OneTimeTaskFactory


class ReportAdminTestCase(TestCase):
    """Test case for ``ReportAdmin`` class"""

    def setUp(self):
        self.report = OneTimeReportFactory(
            task=OneTimeTaskFactory(rules=[RuleFactory()]),
            passed_rules=[RuleFactory()])

        self.admin = ReportAdmin(Report, AdminSite())

    def test_passed_rules_count(self):
        """Ensure that passed rules count equals count of ``passed_rules`` of
        model instance
        """
        self.assertEqual(self.admin.passed_rules_count(self.report),
                         self.report.passed_rules.count())

    def test_total_rules_count(self):
        """Ensure that total_rules_count executes ``get_all_rules`` method"""
        self.assertEqual(self.admin.total_rules_count(self.report),
                         self.report.task.get_all_rules().count())
