import time
import psutil
import json
from flask import Flask, jsonify

app = Flask(__name__)

class PerformanceMonitor:
    """
    A class used to monitor system performance in real-time.

    ...

    Attributes
    ----------
    cpu_usage : float
        the current CPU usage as a percentage
    memory_usage : float
        the current memory usage as a percentage
    disk_usage : float
        the current disk usage as a percentage
    network_usage : float
        the current network usage as a percentage

    Methods
    -------
    update_metrics():
        Updates the performance metrics.
    """

    def __init__(self):
        self.cpu_usage = 0
        self.memory_usage = 0
        self.disk_usage = 0
        self.network_usage = 0

    def update_metrics(self):
        """Updates the performance metrics."""
        self.cpu_usage = psutil.cpu_percent()
        self.memory_usage = psutil.virtual_memory().percent
        self.disk_usage = psutil.disk_usage('/').percent
        self.network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

monitor = PerformanceMonitor()

@app.route('/api/v1/performance-data', methods=['GET'])
def get_performance_data():
    """Returns the current performance data."""
    monitor.update_metrics()
    return jsonify({
        'cpu_usage': monitor.cpu_usage,
        'memory_usage': monitor.memory_usage,
        'disk_usage': monitor.disk_usage,
        'network_usage': monitor.network_usage
    })

if __name__ == '__main__':
    app.run(debug=True)