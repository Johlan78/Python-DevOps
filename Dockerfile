# Utiliser une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans l'image
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000 (port par défaut pour Flask)
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["python", "app.py"]
