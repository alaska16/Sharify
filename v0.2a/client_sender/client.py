# following this tutorial : https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
# CLIENT_SENDER
# Envoie l'URL d'un titre Spotify (pour plus tard : pouvoir partager playlists)

print("Sharify Client v0.2a")
print("21SEP22")
import socket
import os
import tqdm
print("Librairies chargées.")

# Variables (pour plus tard, sera modifiable dans les paramètres)
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # faire tests pr savoir quelle taille est optimale
# connexionok = False

# Addresses IP et métadonnées
host = "127.0.0.1"
port = 5555
filename = "Spotify_Code.png" 
filesize = os.path.getsize(filename)

# TCP et connexion
sender = socket.socket()

# Boucle for pour pouvoir réitérer la connexion plusieurs fois en cas d'échec
try:
    print(f"Connexion à {host}:{port} en cours...")
    sender.connect((host, int(port)))
    # connexionok = True
    print("Connecté avec succès.")
    sender.send(f"{filename}{SEPARATOR}{filesize}".encode())
    #envoi du fichier
    progress = tqdm.tqdm(range(filesize), f"Envoi de {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as spotifycode:
        while True:
            bytes_read = spotifycode.read(BUFFER_SIZE) #lecture depuis le fichier
            if not bytes_read:
                break #quand transmission s'arrête, stop
            sender.sendall(bytes_read) #envoyer les octets du buffer (?)
            progress.update(len(bytes_read))
    sender.close()
except ConnectionRefusedError: # Je ne comprends pas d'où vient OSError, à voir
    print("Le client n'a pas pu se connecter au serveur, vérifier vos paramètres de connexion.")
    pass
