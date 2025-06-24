This monitor would poll available devices and provide status real time

device_monitor/
├── app.py               # Main Flask app
├── devices.json         # Persisted device list
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build file
├── docker-compose.yml   # Docker Compose file
├── prometheus.yml       # Prometheus config
├── templates/
│   └── index.html       # Web dashboard (commissioning)
├── README.md            # Deployment instructions
└── device_monitoring.deb # (Built later)