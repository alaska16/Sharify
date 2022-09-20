# SERVER_RECEIVER
# Sharify Server v0.1.1a, 21/09/2022
# POUR PLUS TARD : récupération des métadonnées depuis internet
import os
import tqdm
import socket
import logging
logging.basicConfig(format='%(asctime)s %(message)s', filename='server.log', encoding='utf-8', level=logging.DEBUG)
logging.info("Chargement des librairies terminé.")
print("Librairies chargées.")
# Variables
SERVER_HOST = "0.0.0.0"
logging.info("Le serveur est configuré pour écouter sur toutes les adresses IP de cette machine.")
SERVER_PORT = 5555
BUFFER_SIZE = 4096
logging.info("Buffer size : 4096")
SEPARATOR = "<SEPARATOR>"
# Gestion du socket
receiver = socket.socket()
logging.info("Socket créé.")
receiver.bind((SERVER_HOST, SERVER_PORT))
receiver.listen(1)
logging.info(f"Écoute sur {SERVER_HOST}:{SERVER_PORT}.")
print(f"En attente sur {SERVER_HOST}:{SERVER_PORT}.")
while True:
    sender, address = receiver.accept()
    logging.info("Connexion acceptée.")
    print("Connexion acceptée.")
    # Réception
    logging.info("Début de la réception du fichier...")
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
            logging.info("Écriture du fichier.")
            progress.update(len(bytes_read))
    sender.close()
    receiver.close()
    logging.info("Fermeture des sockets.")
    break