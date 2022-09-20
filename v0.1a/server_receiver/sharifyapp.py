# DISPLAY_RECEIVER

# Informations
print("Sharify Server v0.02-a, Ali KHELFAOUI (2022)")
print("Date : 20SEP2022")

# Fonctions
def interface():
    
    pygame.draw.line(screen, r, (0, 160), (640, 160))

# Variables 
connected = False
# code_ok = True
# code_ko = False
# code_waiting = True # Ajouter condition si codes précédemment enregistrés, alors False
running = True
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
b = (0, 0, 255)

# Chargement et initialisation des libraries
import pygame
import socket
import tqdm
import os
# import logging
pygame.init()
# logging.basicConfig(filename="latest.log", level=logging.DEBUG)
print("Libraries chargées et initialisées.")
pygame.display.set_caption("Sharify v0.1-a")

# Initialisation écran
screen = pygame.display.set_mode((screen_width, screen_height))

# Boucle principale
while running:
    if connected == False:
        spotifybar = pygame.image.load("Spotify_Code_waiting.png")
        interface()
        screen.blit(spotifybar, (0, 0))
        pygame.display.flip()
    for event in pygame.event.get():
        os.system("python3 server.py")
        spotifybar = pygame.image.load("Spotify_Code.png")
        screen.blit(spotifybar, (0, 0))        
        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False