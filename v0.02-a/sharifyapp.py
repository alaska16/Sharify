# Système de log
# créer un dossier logs puis écrire vers latest.log
# anciens latest.log deviennen† JJMMAAHHMM.log


# Informations
print("Sharify v0.02-a, Ali KHELFAOUI (2022)")
print("Date : 13SEP2022")

# Chargement et initialisation des libraries
import pygame
import socket
import tqdm
import os
pygame.init()
print("Libraries chargées et initialisées.")
pygame.display.set_caption("Sharify v0.02-a")

# Écran
screen_width = 640
screen_height = 160
screen = pygame.display.set_mode((screen_width, screen_height))

# Code Spotify
spotifybar = pygame.image.load("Spotify_Code_empty.png")
screen.blit(spotifybar, (0, 0))
pygame.display.flip()

# Boucle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False