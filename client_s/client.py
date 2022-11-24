# Following this tutorial : https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
# CLIENT_SENDER
# Envoie l'URL d'un titre Spotify (pour plus tard : pouvoir partager playlists)

print("Sharify Client v0.2a")
print("24NOV22")
import socket
import os
import tqdm
import requests
print("Librairies chargées.")

# Variables (pour plus tard, sera modifiable dans les paramètres)
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
track_id = "notset" # Utiliser l'API Spotify pour obtenir l'ID du titre
base_url = "https://scannables.scdn.co/uri/plain/png/000000/white/640/spotify:track:" # 22 caractères : envoi des 22 derniers caractères à server.py puis télécharger code spotify avec scannables

# Addresses IP, métadonnées et téléchargement du code depuis Spotify
host = "127.0.0.1"
port = 5555
# track_id = url[-22:]
track_id = input("Track ID : ") # Temporaire : ici ajouter récupération du Track ID (et métadonnées) depuis API Spotify
url = base_url + track_id
print(track_id)
print(url)
spotifycode = requests.get(url).content
with open('Spotify_Code.png', 'wb') as download:
    download.write(spotifycode) 
print("Téléchargement du code Spotify terminé.")
filename = "Spotify_Code.png"
filesize = os.path.getsize(filename)

# TCP et connexion
sender = socket.socket()

# Pour plus tard : boucle for pour pouvoir réitérer la connexion plusieurs fois en cas d'échec
try:
    print(f"Connexion à {host}:{port} en cours...")
    sender.connect((host, int(port)))
    print("Connecté avec succès.")
    sender.send(f"{filename}{SEPARATOR}{filesize}".encode())
    # Envoi du fichier
    progress = tqdm.tqdm(range(filesize), f"Envoi de {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as spotifycode:
        while True:
            bytes_read = spotifycode.read(BUFFER_SIZE) #lecture depuis le fichier
            if not bytes_read:
                break # Arrêt de la transmission
            sender.sendall(bytes_read) #envoyer les octets du buffer (?)
            progress.update(len(bytes_read))
    sender.close()
except ConnectionRefusedError: # Je ne comprends pas d'où vient OSError, à voir
    print("Le client n'a pas pu se connecter au serveur, vérifiez vos paramètres de connexion.")
    pass
