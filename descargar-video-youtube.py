from pytube import YouTube
import os
import re
import urllib.request

def download_video(url):
    yt = YouTube(url)
    
    # Descargar el video
    stream = yt.streams.get_highest_resolution()
    title = yt.title
    # Limpiar el título de caracteres no válidos para nombres de archivo en Windows
    title = re.sub(r'[\\/:*?"<>|]', '', title)
    stream.download(filename=f"{title}.mp4")
    
    # Descargar la imagen de portada
    thumbnail_url = yt.thumbnail_url
    thumbnail_data = urllib.request.urlopen(thumbnail_url).read()
    with open(f"{title}_thumbnail.jpg", "wb") as file:
        file.write(thumbnail_data)
    
    print("El video y la imagen de portada han sido descargados correctamente.")

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=M7v2jXR-Jlk"

download_video(url)
