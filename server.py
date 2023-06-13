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
