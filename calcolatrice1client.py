import json
import socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 4004
BUFFER_SIZE = 1024
NUM_MESSAGES = 5
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(5):
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = input("Inserisci l'operazione (simbolo)")
    secondoNumero = float(input("Inserisci il secondo numero:"))
    messaggio = {"primoNumero":primoNumero,
                "operazione":operazione,
                "secondoNumero" : secondoNumero}
    messaggio = json.dumps(messaggio)
    sock.sendto(messaggio.encode(), (SERVER_IP, 4004))
    print(f"Messaggio inviato al server: {messaggio}")

    # Ricezione della risposta dal server
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto dal server {addr}: {data.decode()}")

sock.close()