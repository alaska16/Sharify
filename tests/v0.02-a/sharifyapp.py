# SERVER_RECEIVER

# Système de log
# créer un dossier logs puis écrire vers latest.log
# anciens latest.log deviennen† JJMMAAHHMM.log

# Informations
print("Sharify Server v0.02-a, Ali KHELFAOUI (2022)")
print("Date : 16SEP2022")

# Chargement et initialisation des libraries
import pygame
import socket
import tqdm
import os
pygame.init()
print("Libraries chargées et initialisées.")
pygame.display.set_caption("Sharify v0.02-a")

# Réseau
SERVER_HOST = "0.0.0.0" # Cette machine
SERVER_PORT = 5555
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
# Connexion
sharify_connect_receiver = socket.socket()
sharify_connect_receiver.bind((SERVER_HOST, SERVER_PORT))
sharify_connect_receiver.listen(10)
print(f"En attente... ({SERVER_HOST} sur le port {SERVER_PORT})")
socket_sender, address = sharify_connect_receiver.accept()
print(f"Connecté à {address}.")
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

# Écran
screen_width = 640
screen_height = 160
screen = pygame.display.set_mode((screen_width, screen_height))

# Code Spotify
spotifybar = pygame.image.load("Spotify_Code_empty.png")
screen.blit(spotifybar, (0, 0))
pygame.display.flip()

# Boucle (pour plus tard : intégrer réseau dans la boucle)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False