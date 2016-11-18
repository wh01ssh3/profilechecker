from rest_framework.test import APITestCase

from apps.schedule.factories import OneTimeTaskFactory, PeriodicTaskFactory


class OneTimeTaskViewSetTestCase(APITestCase):
    """Test case for ``OneTimeTaskViewSet``"""

    def setUp(self):
        self.task = OneTimeTaskFactory()
        self.another_task = OneTimeTaskFactory()

        self.client.force_authenticate(self.task.user)
        self.url = '/api/schedule/one-time-tasks/'

    def test_task_list(self):
        """Ensure that user can see only his tasks"""
        resp = self.client.get(self.url)
        self.assertEqual(len(resp.data), 1)


class PeriodicTaskViewSetTestCase(APITestCase):
    """Test case for ``PeriodicTaskViewSet``"""

    def setUp(self):
        self.task = PeriodicTaskFactory()
        self.another_task = PeriodicTaskFactory()

        self.client.force_authenticate(self.task.user)
        self.url = '/api/schedule/periodic-tasks/'

    def test_task_list(self):
        """Ensure that user can see only his tasks"""
        resp = self.client.get(self.url)
        self.assertEqual(len(resp.data), 1)
