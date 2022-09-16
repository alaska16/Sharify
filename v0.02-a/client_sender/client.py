# following this tutorial : https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
#CLIENT_SENDER
print("Sharify Client v0.02-a")
print("16SEP22")
import socket
import os
import tqdm
print("Librairies chargées.")

# Variables (pour plus tard, sera modifiable dans les paramètres)
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # faire tests pr savoir quelle taille est optimale

# Addresses IP et métadonnées
host = "127.0.0.1" # La machine qui reçoit le code
port = 5555 #à terme, sera le port 80 (jsais pas si c'est possible, à voir)
filename = "Spotify_Code.png" 
filesize = os.path.getsize(filename)

# TCP et connexion
sharify_connect_sender = socket.socket()
print(f"Connexion à {host}:{port} en cours...") #ajouter condition après cette ligne en cas d'erreur pr afficher message d'erreur
sharify_connect_sender.connect((host, int(port))) #port doit être un integer
print("Connecté avec succès.")

sharify_connect_sender.send(f"{filename}{SEPARATOR}{filesize}".encode())#tbh jcomprends pas comment le serveur recoit cette string (?) en comprenant tout de suite que c'est une string

#envoi du fichier
progress = tqdm.tqdm(range(filesize), f"Envoi de {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as spotifycode:
    while True:
        bytes_read = spotifycode.read(BUFFER_SIZE) #lecture depuis le fichier
        if not bytes_read:
            break #quand transmission s'arrête, stop
        sharify_connect_sender.sendall(bytes_read) #envoyer les octets du buffer (?)
        progress.update(len(bytes_read))
sharify_connect_sender.close()
