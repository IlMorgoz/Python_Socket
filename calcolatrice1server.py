import socket
import json

SERVER_IP ="127.0.0.1"
SERVER_PORT = 4004 #porta modificata dati problemi di compatibilità con la porta 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, 4004))
#Ricevo i dati
print("Server avviato")
while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    if not data:
        print("Misba")
        break
    
    data = data.decode()
    print(f"Messaggio ricevuto dal client {addr}: {data}")
    data = json.loads(data)
    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]
    if operazione == "+":
        risultato = primoNumero + secondoNumero
    elif operazione == "-":
        risultato = primoNumero - secondoNumero
    elif operazione == "*":
        risultato = primoNumero * secondoNumero
    elif operazione == "/":
        if secondoNumero != 0:
            risultato = primoNumero / secondoNumero
        else:
            risultato = "Errore: divisione per zero"
    else:
        risultato = "Operazione non valida"

    # Invio della risposta al client
    sock.sendto(str(risultato).encode(), addr)