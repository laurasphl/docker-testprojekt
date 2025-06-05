# Basis-Image mit Python
FROM python:3.11-slim

# Verzeichnis im Container anlegen
WORKDIR /app

# Sicherstellen, dass pip aktuell ist
RUN pip install --upgrade pip

# Notwendige Pakete installieren
RUN pip install numpy pandas matplotlib seaborn

# (Optional) Startbefehl oder CMD-Zeile hier ergänzen, z. B. ein Skript ausführen
# CMD ["python", "main.py"]