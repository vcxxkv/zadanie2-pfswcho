Wykonanie: Krystian Wypart
Nr albumu: 91187

Zadanie 1 
Kod serwera - server.py

from flask import Flask, request
import datetime
import socket

app = Flask(__name__)

# Pobranie aktualnej daty i godziny
def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Adres IP klienta
def get_client_ip():
    return request.remote_addr

# Główna strona klienta
@app.route('/')
def index():
    client_ip = get_client_ip()
    current_time = get_current_time()
    return f"Adres IP klienta: {client_ip}<br>Aktualny czas: {current_time}"

if __name__ == '__main__':
    # Informacje o autorze serwera
    author_name = "Krystian Wypart"
    server_port = 8080
    server_host = '0.0.0.0'

    # Logowanie informacji przy uruchomieniu serwera
    current_time = get_current_time()
    print(f"Serwer uruchomiony przez: {author_name}")
    print(f"Data uruchomienia: {current_time}")
    print(f"Serwer nasłuchuje na porcie: {server_port}")

    # Uruchomienie serwera Flask
    app.run(port=server_port, host=server_host)


Zadanie 2.
Kod pliku Dockerfile


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


Zadanie 3 - Naley podać polecenia niezbędna do:

a) Zbudowania opracowanego obrazu kontenera - 

docker build -t server-image

b) uruchomienie konternera na podstawie zbudowanego obrazu-

docker run -d -p 8080:8080 --name server-container server-image

c) sposobu uzyskania informacji, które wygenerował serwer w trakcie uruchamiania 
kontenera(patrz: punkt 1a)-

if __name__ == '__main__':
    # Informacje o autorze serwera
    author_name = "Krystian Wypart"
    server_port = 8080
    server_host = '0.0.0.0'

    # Logowanie informacji przy uruchomieniu serwera
    current_time = get_current_time()
    print(f"Serwer uruchomiony przez: {author_name}")
    print(f"Data uruchomienia: {current_time}")
    print(f"Serwer nasłuchuje na porcie: {server_port}")

    Informacje dostępne w Docker Desktop > Containers > po wybraniu kontenera > Logs

    d) Sprawdzenia, ile wartw posiada zbudowany obraz-
    docker history server-image


    
