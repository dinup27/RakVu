from flask import Flask, render_template, jsonify, Response, request, redirect, url_for
from ping3 import ping
from pysnmp.hlapi import *
from prometheus_client import Gauge, generate_latest
import json
import os

app = Flask(__name__)

USERNAME = 'admin'
PASSWORD = 'admin'

DEVICE_FILE = 'devices.json'
DEVICES = {}

# SNMP OIDs and Prometheus Gauges (same as previous version)
# [OIDs, Vendor Detection, Device Type Detection remain unchanged]

def load_devices():
    global DEVICES
    if os.path.exists(DEVICE_FILE):
        with open(DEVICE_FILE, 'r') as f:
            DEVICES = json.load(f)

def save_devices():
    with open(DEVICE_FILE, 'w') as f:
        json.dump(DEVICES, f, indent=2)

# Authentication logic unchanged

@app.route("/")
@requires_auth
def index():
    grouped_devices = {'Switch': [], 'Server': [], 'Storage': [], 'Unknown': []}
    for name, info in DEVICES.items():
        grouped_devices[info.get('type', 'Unknown')].append({'name': name, 'ip': info['ip']})
    return render_template("index.html", devices=grouped_devices)

@app.route("/add_device", methods=["POST"])
@requires_auth
def add_device():
    name = request.form.get("name")
    ip = request.form.get("ip")
    if name and ip:
        DEVICES[name] = {"ip": ip}
        save_devices()
    return redirect(url_for("index"))

@app.route("/status")
@requires_auth
def status():
    return jsonify(get_device_status())

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

# Device status logic (same as previous version)

if __name__ == "__main__":
    load_devices()
    app.run(host="0.0.0.0", port=5000)
