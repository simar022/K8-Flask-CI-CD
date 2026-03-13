#!/bin/bash

DOMAIN="myapp.local"
MINIKUBE_IP=$(minikube ip)

echo "🔧 Automating DNS for $DOMAIN at $MINIKUBE_IP..."

# 1. Update /etc/hosts (Requires sudo privileges for the runner user)
if grep -q "$DOMAIN" /etc/hosts; then
    sudo sed -i "s/.*$DOMAIN/$MINIKUBE_IP $DOMAIN/" /etc/hosts
else
    echo "$MINIKUBE_IP $DOMAIN" | sudo tee -a /etc/hosts
fi

# 2. Check if tunnel is running, if not, notify or start in background
if ! pgrep -x "minikube" > /dev/null; then
    echo "⚠️ Minikube tunnel is not running. Starting in background..."
    nohup minikube tunnel > /dev/null 2>&1 &
    sleep 5
fi

echo "🚀 Success! Dashboard is live at: https://$DOMAIN"
