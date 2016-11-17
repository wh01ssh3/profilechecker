from django.contrib.admin import AdminSite
from django.test import TestCase

from ..admin import ReportAdmin
from ..factories import OneTimeReportFactory
from ..models import Report
from ...rules.factories import ProfileFactory, RuleFactory
from ...schedule.factories import OneTimeTaskFactory


# TODO: move these test cases into test_models.py

class ReportAdminTestCase(TestCase):
    """Test case for ``ReportAdmin`` class"""

    def setUp(self):
        # Create 3 rules
        self.rules = RuleFactory.create_batch(3)

        # Create profile which includes all 3 rules
        self.profile = ProfileFactory(rules=self.rules)

        # Create profile which includes 2 tasks
        self.another_profile = ProfileFactory(rules=self.rules[0:1])

        # Create one time task which includes 1 profile
        self.task = OneTimeTaskFactory(profiles=(self.profile,))

        # Create task with 2-task profile and 2 rules which is crossed with
        # profile rules
        self.another_task = OneTimeTaskFactory(
            profiles=(self.another_profile,), rules=self.rules[1:2])

        # Create task with 2-task profile and 1 rule which is not included in
        # profile
        self.another_different_task = OneTimeTaskFactory(
            profiles=(self.another_profile,), rules=(self.rules[2],))

        # Create report
        self.report = OneTimeReportFactory(task=self.task,
                                           passed_rules=self.rules[0:1])

        # Another report
        self.another_report = OneTimeReportFactory(
            task=self.another_task,
            passed_rules=self.rules[0:1]
        )

        # Another different report
        self.another_different_report = OneTimeReportFactory(
            task=self.another_different_task,
            passed_rules=self.rules[0:1]
        )

        # Create admin instance
        self.admin = ReportAdmin(Report, AdminSite())

    def test_passed_rules_count(self):
        """Ensure that passed rules count equals count of ``passed_rules`` of
        model instance
        """
        self.assertEqual(self.admin.passed_rules_count(self.report),
                         self.report.passed_rules.count())

    def test_total_rules_count_all_rules_from_profile(self):
        """Ensure that all rules from profile counts when
        ``total_rules_count`` calls
        """
        self.assertEqual(self.admin.total_rules_count(self.report),
                         len(self.rules))

    def test_total_rules_count_another_report(self):
        """Test 1 profile and 2 rules, one of those in profile """
        self.assertEqual(
            self.admin.total_rules_count(self.another_report),
            len(self.rules) - 1)

    def test_total_rules_count_another_different_report(self):
        """Test 1 profile and 1 rule, which not in profile"""
        self.assertEqual(
            self.admin.total_rules_count(self.another_different_report),
            len(self.rules) - 1)
