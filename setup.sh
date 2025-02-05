#!/bin/bash

# Build and run tests
# Arrêter les conteneurs en cours d'exécution (optionnel)
export LOG=1
echo "Arrêt des conteneurs en cours..."
docker-compose down

# Construire les images Docker
echo "Construction des images Docker..."
docker build -t docker_base:latest  ./base
docker build -t docker_authentication:latest  ./authentication_test
docker build -t docker_authorization:latest  ./authorization_test
docker build -t docker_content:latest  ./content_test


# Démarrer les conteneurs avec Docker Compose
echo "Démarrage des conteneurs..."
docker-compose up -d --build

#Affichage des logs
docker logs -f test_authorization
docker logs -f test_authentication
docker logs -f test_content


# Vérifier si tout fonctionne
echo "Conteneurs en cours d'exécution :"
docker ps