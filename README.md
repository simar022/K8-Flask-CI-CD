# 🚀 K8-Flask-CI-CD

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-blue.svg)](https://kubernetes.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Flask-based DevOps dashboard application deployed on Kubernetes with CI/CD automation. This project demonstrates containerization, orchestration, and monitoring for a simple web service.

---

## 📋 Table of Contents

- [🚀 Overview](#-overview)
- [✨ Features](#-features)
- [🛠 Prerequisites](#-prerequisites)
- [🚀 Installation](#-installation)
- [📖 Usage](#-usage)
- [🏗 Project Structure](#-project-structure)
- [🔧 API Endpoints](#-api-endpoints)
- [🤝 Contributing](#-contributing)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🚀 Overview

This project features a lightweight Flask application that serves a dashboard displaying real-time system metrics such as CPU and RAM usage, pod name, and node IP. It's designed for deployment in Kubernetes environments with built-in health checks, resource limits, and ingress configuration for secure access.

The application is containerized using Docker and includes Kubernetes manifests for seamless deployment, making it an excellent example of modern DevOps practices.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Real-time Metrics Dashboard** | Displays CPU usage, RAM usage, pod name, and node IP |
| 🏥 **Health Checks** | Built-in `/health` endpoint for Kubernetes probes |
| 🔄 **Stress Testing** | `/stress` endpoint to simulate load for HPA testing |
| 🐳 **Docker Containerization** | Optimized Python 3.9 slim image |
| ☸️ **Kubernetes Deployment** | Complete K8s manifests with deployment, service, and ingress |
| 🔒 **SSL/TLS Support** | Ingress configured with SSL redirection |
| 🤖 **Automation Scripts** | Bash script for automating local DNS and tunnel setup |

---

## 🛠 Prerequisites

Before you begin, ensure you have the following installed:

- 🐳 **Docker** (for building and running containers)
- ☸️ **Kubernetes cluster** (minikube for local development)
- 🐍 **Python 3.9** (for local development)
- 🔧 **kubectl** (Kubernetes CLI)
- 🌐 **NGINX Ingress Controller** (for ingress functionality)

---

## 🚀 Installation

Follow these steps to get the project up and running:

### 1. Clone the Repository
```bash
git clone https://github.com/simar022/K8-Flask-CI-CD.git
cd K8-Flask-CI-CD
```

### 2. Build the Docker Image
```bash
docker build -t flask-app:latest .
```

### 3. Deploy to Kubernetes
```bash
kubectl apply -f k8s-deploy.yaml
kubectl apply -f ingress.yaml
```

### 4. Automate Local Access (for Minikube)
```bash
chmod +x automate_access.sh
./automate_access.sh
```

---

## 📖 Usage

Once deployed, you can interact with the application as follows:

- **🌐 Access the Dashboard**: Navigate to `https://myapp.local` in your browser to view the metrics dashboard
- **🏥 Health Check**: Visit `https://myapp.local/health` for a JSON status response
- **🔄 Stress Test**: Access `https://myapp.local/stress` to trigger CPU load and test horizontal pod autoscaling

---

## 🏗 Project Structure

```
K8-Flask-CI-CD/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container build instructions
├── k8s-deploy.yaml       # Kubernetes deployment manifests
├── ingress.yaml          # Ingress configuration
├── automate_access.sh    # Local development automation script
└── README.md             # Project documentation
```

---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Renders the main dashboard with system metrics |
| `/health` | GET | Returns JSON health status (`{"status": "UP"}`) |
| `/stress` | GET | Triggers CPU-intensive operation for load testing |

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Commit your changes (`git commit -m 'Add some amazing feature'`)
4. 🚀 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

---

## 🙏 Acknowledgments

- 🐍 **Flask** - The web framework used
- 📊 **psutil** - For system metrics collection
- ☸️ **Kubernetes** - Container orchestration platform
- 🌐 **NGINX Ingress** - Load balancing and SSL termination

---
