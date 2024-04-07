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
    
    print(f"El video '{title}' y la imagen de portada han sido descargados correctamente.")

# Lista de URLs de videos de YouTube
urls = [
    "https://www.youtube.com/watch?v=LfwVGlW237o",
    "https://www.youtube.com/watch?v=7-v3ckbGSrM",
    "https://www.youtube.com/watch?v=oM2o_OY3mAk",
    "https://www.youtube.com/watch?v=vsAJHkv3Iys",
    "https://www.youtube.com/watch?v=s1URBn3PQTI",
    "https://www.youtube.com/watch?v=lFyxExUoAJY",
    "https://www.youtube.com/watch?v=LpTdmXOfORs",
    "https://www.youtube.com/watch?v=8pfkcG9dSEE",
    "https://www.youtube.com/watch?v=-r687V8yqKY",
    "https://www.youtube.com/watch?v=ygA84G7aVPg",
    "https://www.youtube.com/watch?v=L50Ie4CxOCk",
]

# Procesar cada URL
for url in urls:
    download_video(url)
