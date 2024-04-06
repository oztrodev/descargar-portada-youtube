from pytube import YouTube
import urllib.request
from datetime import datetime

def download_thumbnail(url):
    yt = YouTube(url)
    thumbnail_url = yt.thumbnail_url
    today = datetime.today().strftime('%Y%m%d')
    filename = f"thumbnail_{today}.jpg"
    urllib.request.urlretrieve(thumbnail_url, filename)
    print(f"La imagen de portada ha sido descargada correctamente como '{filename}'.")

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=BtGXjI1mxp4&t=600s"

download_thumbnail(url)
