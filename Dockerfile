FROM python:3.11-slim

# Lege das Arbeitsverzeichnis im Container auf /app fest → alle weiteren Befehle und Pfade beziehen sich auf /app
WORKDIR /app

# Aktualisiere pip (den Python-Paketmanager) auf neueste Version
# Installiere die benötigten Python-Bibliotheken: - numpy, pandas, matplotlib, seaborn (laut Aufgabe c) - pytest (für die automatisierten Tests in Aufgabe a und d)
RUN pip install --upgrade pip && \
    pip install numpy pandas matplotlib seaborn pytest

# Erweitere den Python-Modulpfad um das Verzeichnis /app/src → dadurch kann man z. B. "from src.find_unique import ..." machen, obwohl src nicht im Standardpfad liegt
ENV PYTHONPATH="${PYTHONPATH}:/app/src"
