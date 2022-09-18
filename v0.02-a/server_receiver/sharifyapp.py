# SERVER_RECEIVER

# Variables 
connected = False
code_ok = False
code_ko = False
code_waiting = True # Ajouter condition si codes précédemment enregistrés, alors False
running = True
# Réseau
SERVER_HOST = "0.0.0.0" # Cette machine
SERVER_PORT = 5555
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
# Écran
screen_width = 640
screen_height = 160

# Fonctions
def connexion(): # Ajouter documentation
    sharify_connect_receiver = socket.socket()
    sharify_connect_receiver.setblocking(0)
    sharify_connect_receiver.bind((SERVER_HOST, SERVER_PORT))
    sharify_connect_receiver.listen(10)
    logging.info(f"En attente... ({SERVER_HOST} sur le port {SERVER_PORT})")
    while True: # Boucle sans conditions
        try:
            socket_sender, address = sharify_connect_receiver.accept()
            logging.info(f"Connecté à {address}.")
            connected = True
            break
        except BlockingIOError: # Si cette erreur est détectée, alors ...
            logging.error("Erreur.")
            socket_sender = 0
            address = 0
            connected = False
            break
    return sharify_connect_receiver, socket_sender, connected

def reception_png(): # Ajouter documentation
    # Échange de métadonnées
    received_metadata = socket_sender.recv(BUFFER_SIZE).decode() # Précédente erreur due à une confusion entre sockets (socket_sender et non pas sharify_...)
    filename, filesize = received_metadata.split(SEPARATOR)
    filename = os.path.basename(filename) # Supprime le chemin d'accès du nom du fichier reçu
    filesize = int(filesize)
    # Réception du fichier
    progress = tqdm.tqdm(range(filesize), f"Réception de {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as spotifycode:
        while True:
            bytes_read = socket_sender.recv(BUFFER_SIZE) # Précédente erreur due à une confusion entre sockets (socket_sender et non pas sharify_...)
            if not bytes_read:
                break
            spotifycode.write(bytes_read)
            progress.update(len(bytes_read))
            socket_sender.close()
            sharify_connect_receiver.close()
    # Ajouter condition si code_ko (erreur)
    # Ajouter condition si code_waiting (en attente de connexion ET aucun code précédemment enregistré)

# Chargement et initialisation des libraries
import pygame
import socket
import tqdm
import os
import logging
pygame.init()
logging.basicConfig(filename="latest.log", level=logging.DEBUG)
logging.info("Libraries chargées et initialisées.")
pygame.display.set_caption("Sharify v0.02-a")
# Informations
logging.info("Sharify Server v0.02-a, Ali KHELFAOUI (2022)")
logging.info("Date : 18SEP2022")

# Initialisation écran
screen = pygame.display.set_mode((screen_width, screen_height))

# Temporaire : connexion (en attendant de faire fonctionner la fonction connexion())
# sharify_connect_receiver = socket.socket()
# sharify_connect_receiver.bind((SERVER_HOST, SERVER_PORT))
# sharify_connect_receiver.listen(10)
# logging.info(f"En attente... ({SERVER_HOST} sur le port {SERVER_PORT})")
# logging.info(f"Connecté à {address}.")
# connected = True
# reception_png()
# code_ok = True

# Boucle principale
while running:
    if connected == False:
        spotifybar = pygame.image.load("Spotify_Code_waiting.png")
        screen.blit(spotifybar, (0, 0))
        pygame.display.flip()
        connexion()
    if connected == True:
        # Affichage du Code Spotify
        if code_ok:
            spotifybar = pygame.image.load("Spotify_Code.png")
            screen.blit(spotifybar, (0,0))
            pygame.display.flip()
        elif code_ko:
            spotifybar = pygame.image.load("Spotify_Code_ko.png")
            screen.blit(spotifybar, (0,0))
            pygame.display.flip()
    for event in pygame.event.get():
        # screen.blit(spotifybar, (0, 0))        
        # pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False