import os
import socket
import time
import psutil
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Basic HTML template for the dashboard
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Dashboard</title>
    <style>
        body { font-family: sans-serif; background: #121212; color: #00ff00; padding: 20px; }
        .card { border: 1px solid #333; padding: 20px; border-radius: 8px; background: #1e1e1e; }
        .metric { font-size: 1.2em; margin: 10px 0; }
        .highlight { color: #00d4ff; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Production Node Dashboard</h1>
        <div class="metric">Pod Name: <span class="highlight">{{ pod_name }}</span></div>
        <div class="metric">Node IP: <span class="highlight">{{ node_ip }}</span></div>
        <div class="metric">CPU Usage: <span class="highlight">{{ cpu }}%</span></div>
        <div class="metric">RAM Usage: <span class="highlight">{{ ram }}%</span></div>
        <hr>
        <p>Access <code>/stress</code> to trigger HPA scaling.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    stats = {
        'pod_name': socket.gethostname(),
        'node_ip': socket.gethostbyname(socket.gethostname()),
        'cpu': psutil.cpu_percent(interval=0.1),
        'ram': psutil.virtual_memory().percent
    }
    return render_template_string(HTML_TEMPLATE, **stats)

@app.route('/health')
def health():
    return jsonify(status="UP"), 200

@app.route('/stress')
def stress():
    # Simulate CPU intensive task for 5 seconds
    end_time = time.time() + 5
    while time.time() < end_time:
        _ = 1000 * 1000
    return jsonify(message="Stress test complete on " + socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
