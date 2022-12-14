# DISPLAY_RECEIVER

# Informations
print("Sharify Server v0.2a, Ali KHELFAOUI (2022)")
print("Date : 24NOV2022")

# Fonctions
def interface_attente():    
    pygame.draw.line(screen, r, (0, 160), (640, 160))
    attente = font.render("En attente...", True, w)
    screen.blit(attente, (8, 200))
def interface(titre_musique, titre_album, artiste, message): # Paramètres : variable titre musique, artiste, AJOUTER GESTION DE L'ECRAN TACTILE ET LES MENUS
    albumcover = pygame.image.load("placeholder128.png")
    pygame.draw.line(screen, gspotify, (0, 160), (640, 160))
    titrem_interface = font.render(titre_musique, True, w)
    titrea_interface = font.render(titre_album, True, w)
    artiste_interface = font.render(artiste, True, w)
    message = font.render(message, True, gspotify)
    screen.blit(titrem_interface, (200, 200))
    screen.blit(titrea_interface, (200, 250))
    screen.blit(artiste_interface, (200, 300))
    screen.blit(albumcover, (8, 200))
    screen.blit(message, (200, 350))

# Variables 
connected = False
running = True
message = "Message personnalisé"
#titre_musique = "0"
#titre_album = "1"
#artiste = "2"
# code_ok = True
# code_ko = False
# code_waiting = True # Ajouter condition si codes précédemment enregistrés, alors False
# Réseau
SERVER_HOST = "0.0.0.0" # Cette machine
SERVER_PORT = 5555
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
# Écran
screen_width = 640
screen_height = 400
r = (255, 0, 0)
g = (0, 255, 0)
gspotify = (30, 215, 96)
b = (0, 0, 255)
w = (255, 255, 255)

# Chargement et initialisation des libraries
# import socket
# import tqdm
# import os
# import subprocess
# logging.basicConfig(filename="latest.log", level=logging.DEBUG)
import pygame
import threading
import logging
from subprocess import call
logging.basicConfig(filename='sharifyapp.log', encoding='utf-8', level=logging.DEBUG)
pygame.init()
logging.info("Chargement et initialisation des librairies terminée.")
print("Libraries chargées et initialisées.")
font = pygame.font.Font(None, 32)
pygame.display.set_caption("Sharify v0.2a")

# Lancement du serveur
def launch_server():
    call(["python", "server_r/server.py"])
serverThread = threading.Thread(target=launch_server)
serverThread.start()
logging.info("Initalisation du serveur terminée.")
print("Serveur initialisé.")

# Initialisation écran
screen = pygame.display.set_mode((screen_width, screen_height))

# Boucle principale
while running:
    for event in pygame.event.get(): 
        try:
            spotifybar = pygame.image.load("Spotify_Code.png")
            screen.blit(spotifybar, (0, 0))
            interface("Titre morceau", "Titre album", "Nom de l'artiste", message)        
            pygame.display.flip()
        except FileNotFoundError:
            spotifybar = pygame.image.load("server_r/Spotify_Code_empty.png")
            screen.blit(spotifybar, (0, 0))
            interface_attente()        
            pygame.display.flip()
        if event.type == pygame.QUIT:
            # Pour plus tard : stopper le subprocess
            running = False