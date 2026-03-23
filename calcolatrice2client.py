import json
import socket
BUFFER_SIZE = 1024
HOST ='127.0.0.1' # Indirizzo del server
PORT = 65432 # Porta usata dal server

primoNumero = float(input("Inserisci il primo numero: "))
operazione = input("Inserisci l'operazione (simbolo)")
secondoNumero = float(input("Inserisci il secondo numero:"))
messaggio = {"primoNumero": primoNumero,
             "operazione": operazione,
             "secondoNumero": secondoNumero}
messaggio = json.dumps(messaggio)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(messaggio.encode())
    print(f"Messaggio inviato al server: {messaggio}")
    data = sock.recv(BUFFER_SIZE) # il parametro indica la dimensione massima dei dati che possono essere ricevuti in una sola volta

    #a questo punto la socket è stata chiusa automaticamente
    print('Received', data.decode())
