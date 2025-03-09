import unittest
from main import PerformanceMonitor

class TestPerformanceMonitor(unittest.TestCase):

    def setUp(self):
        self.monitor = PerformanceMonitor()

    def test_initial_values(self):
        self.assertEqual(self.monitor.cpu_usage, 0)
        self.assertEqual(self.monitor.memory_usage, 0)
        self.assertEqual(self.monitor.disk_usage, 0)
        self.assertEqual(self.monitor.network_usage, 0)

    def test_update_metrics(self):
        self.monitor.update_metrics()
        self.assertNotEqual(self.monitor.cpu_usage, 0)
        self.assertNotEqual(self.monitor.memory_usage, 0)
        self.assertNotEqual(self.monitor.disk_usage, 0)
        self.assertNotEqual(self.monitor.network_usage, 0)

if __name__ == '__main__':
    unittest.main()