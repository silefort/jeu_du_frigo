# Utiliser une image Python officielle légère
FROM python:3.10-slim

# Variables d'environnement pour éviter buffer et définir la variable de prod Flask
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Créer et positionner dans le dossier /app
WORKDIR /app

# Copier requirements.txt et installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code
COPY . /app

# Exposer le port 5000 (port par défaut Flask)
EXPOSE 5000

# Commande pour lancer l'application
CMD ["flask", "run"]
