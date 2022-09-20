# SERVER_RECEIVER
# Sharify Server v0.1-a, 20/09/2022
# Pas de logging pour l'instant
# POUR PLUS TARD : récupération des métadonnées depuis internet
import os
import tqdm
import socket
print("Librairies chargées.")

# Variables
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5555
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
testvariable = 10
# Gestion du socket
receiver = socket.socket()
receiver.bind((SERVER_HOST, SERVER_PORT))
receiver.listen(1)
print(f"En attente sur {SERVER_HOST}:{SERVER_PORT}.")
while True:
    try:
        sender, address = receiver.accept()
        print("Connexion acceptée.")
        # Réception
        received_mdata = sender.recv(BUFFER_SIZE).decode()
        filename, filesize = received_mdata.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)
        progress = tqdm.tqdm(range(filesize), f"Réception du fichier... {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as spotifycode:
            while True: # Essayer plus tard une structure try/except
                bytes_read = sender.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                spotifycode.write(bytes_read)
                progress.update(len(bytes_read))
        sender.close()
        receiver.close()
        break
    except BlockingIOError:
       print("Client non trouvé.")
       pass
