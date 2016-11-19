from rest_framework import status
from rest_framework.test import APITestCase

from ..factories import OneTimeReportFactory
from ...rules.factories import RuleFactory
from ...schedule.factories import (OneTimeTaskFactory, PeriodicTaskFactory,
                                   UserFactory)


class OneTimeReportViewSetTestCase(APITestCase):
    """Test case for ``OneTimeReportViewSet``"""

    def setUp(self):
        # Create users
        self.user = UserFactory()
        self.another_user = UserFactory()
        # Create task with 2 rules
        self.task = OneTimeTaskFactory(rules=[RuleFactory(), RuleFactory()],
                                       user=self.user)

        self.client.force_authenticate(self.user)

        self.url = '/api/reports/one-time-reports/'

        self.data = {
            'task': self.task.id,
            'rules': [
                self.task.rules.all()[0].id
            ]
        }

    def test_user_can_submit_report(self):
        """Test user able to submit a report"""
        resp = self.client.post(self.url, self.data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_user_cant_submit_foreign_report(self):
        """Ensure that user, who's is not task assignee can't submit a report
        """
        self.client.force_authenticate(self.another_user)
        resp = self.client.post(self.url, self.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cant_submit_two_reports(self):
        """Ensure that user can't submit more than one report"""
        OneTimeReportFactory(task=self.task)
        resp = self.client.post(self.url, self.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)


class PeriodicReportViewSetTestCase(APITestCase):
    """Test case for ``PeriodicReportViewSet``"""

    def setUp(self):
        # Create users
        self.user = UserFactory()
        self.another_user = UserFactory()
        # Create task with 2 rules
        self.task = PeriodicTaskFactory(rules=[RuleFactory(), RuleFactory()],
                                        user=self.user)

        self.client.force_authenticate(self.user)

        self.url = '/api/reports/periodic-reports/'

        self.data = {
            'task': self.task.id,
            'rules': [
                self.task.rules.all()[0].id
            ]
        }

    def test_user_can_submit_report(self):
        """Test user able to submit a report"""
        resp = self.client.post(self.url, self.data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_user_cant_submit_foreign_report(self):
        """Ensure that user, who's is not task assignee can't submit a report
        """
        self.client.force_authenticate(self.another_user)
        resp = self.client.post(self.url, self.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
