import socket
import json

IP = "127.0.0.1"
PORTA = 22224
DIM_BUFFER = 1024

# Creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

# Binding della socket alla porta specificata
    sock_server.bind((IP, PORTA))

    # Metti la socket in ascolto per le connessioni in ingresso
    sock_server.listen()

    print(f"Server in ascolto su {IP}:{PORTA} ... ")

    # Loop principale del server
    while True:
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:
            # Leggi i dati inviati dal client
            dati = json.loads(sock_client.recv(DIM_BUFFER).decode())
            if not dati:
                print("Misba")
                break
            print(f"Ricevuto messaggio dal client {sock_client}: {dati}")
            primoNumero = dati["primoNumero"]
            operazione = dati["operazione"]
            secondoNumero = dati["secondoNumero"]
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
            print(f"risultato: {risultato}")
            sock_client.sendall(str(risultato).encode())