
# Etap początkowy budowania
FROM python:3.9-slim as builder

# Skopiowanie pliku serwera
COPY server.py .

# Instalacja zależności
RUN pip install flask

# Etap finalny
FROM python:3.9-slim

# Skopiowanie pliku serwera
COPY --from=builder server.py /app/server.py

# Skopiowanie zależności
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Ustalenie portu
ENV PORT=8080

# Uruchomienie serwera
CMD ["python", "/app/server.py"]