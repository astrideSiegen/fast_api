#!/bin/bash

# Build and run tests
# Arrêter les conteneurs en cours d'exécution (optionnel)
echo "Arrêt des conteneurs en cours..."
docker-compose down

# Construire les images Docker
echo "Construction des images Docker..."
docker build -t docker_authentication:latest  ./authentication_test
docker build -t docker_authorization:latest  ./authorization_test
docker build -t docker_content:latest  ./content_test

# Démarrer les conteneurs avec Docker Compose
echo "Démarrage des conteneurs..."
docker-compose up -d --build

# Vérifier si tout fonctionne
echo "Conteneurs en cours d'exécution :"
docker ps