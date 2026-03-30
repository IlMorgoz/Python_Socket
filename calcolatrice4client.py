# Client TCP multithread che invia NUM_WORKERS richieste contemporanee al server
# Ogni richiesta contiene un'operazione aritmetica da eseguire

import socket, json, random, time, threading

# --- Configurazione ---
HOST = "127.0.0.1"  # IP del server
PORT = 22224  # Porta del server (assicurarsi che il server stia ascoltando su questa)
NUM_WORKERS = 15  # Numero di richieste (thread) da inviare in parallelo
OPERAZIONI = ["+", "-", "*", "/", "%"]  # Lista delle operazioni consentite


# 1 Funzione target assegnata a ciascun thread per connettersi e dialogare con il server
def genera_richieste(address, port):
    # 2 Inizializza un socket IPv4 (AF_INET) di tipo TCP (SOCK_STREAM) con chiusura automatica (with)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((address, port))  # Connessione al server

        # 3 Genera casualmente i due operandi numerici e l'operatore matematico
        primoNumero = random.randint(0, 100)
        operazione = OPERAZIONI[random.randint(0, 3)]  # Scegli operazione a caso (tra le prime 4)
        secondoNumero = random.randint(0, 100)

        # 4 Inserisce i dati in un dizionario Python e lo serializza in una stringa formato JSON
        messaggio = {
            "primoNumero": primoNumero,
            "operazione": operazione,
            "secondoNumero": secondoNumero
        }
        messaggio = json.dumps(messaggio)

        # 5 Codifica la stringa JSON in byte (UTF-8) e si assicura di inviarla per intero al server
        sock_service.sendall(messaggio.encode("UTF-8"))

        # 6 Fa partire il cronometro per misurare il tempo di latenza (attesa della risposta)
        start_time_thread = time.time()

        # 7 Si mette in ascolto sincrono per ricevere la risposta del server (fino a un massimo di 1024 byte)
        data = sock_service.recv(1024)

    # 8 Ferma il cronometro, decodifica i byte ricevuti in stringa e stampa i risultati a schermo
    end_time_thread = time.time()
    print("Received: ", data.decode())
    print(f"{threading.current_thread().name} exec time = ", end_time_thread - start_time_thread)


# --- Punto di ingresso del programma ---
if __name__ == "__main__":
    start_time = time.time()  # Tempo di inizio totale

    # 9 Crea una lista contenente NUM_WORKERS thread, pronti ad eseguire 'genera_richieste'
    threads = [
        threading.Thread(target=genera_richieste, args=(HOST, PORT))
        for _ in range(NUM_WORKERS)
    ]

    # 10 Iterazione che avvia effettivamente tutti i thread in parallelo
    [thread.start() for thread in threads]

    # 11 Mette in attesa il programma principale finché tutti i thread non hanno completato il loro lavoro
    [thread.join() for thread in threads]

    end_time = time.time()  # Tempo di fine totale

    # Stampa il tempo complessivo impiegato per eseguire tutte le richieste
    print("Tempo totale impiegato = ", end_time - start_time)