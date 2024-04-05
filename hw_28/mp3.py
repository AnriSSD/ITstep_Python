import threading
import requests


def download_mp3(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"File {filename} uploaded succesfuly.")


# URL mp3 files list for downloadng
mp3_urls = [
    "https://www.televisiontunes.com/song/download/25691",
    "https://www.televisiontunes.com/song/download/639",
]

# Create threads for each url
for index, url in enumerate(mp3_urls):
    thread = threading.Thread(target=download_mp3, args=(url, f"song{index+1}.mp3"))
    thread.start()
