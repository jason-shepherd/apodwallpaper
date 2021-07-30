import os
import requests
import shutil
import ctypes
import time
from bs4 import BeautifulSoup

def download_image(url):
    response = requests.get(url, stream = True)
    if response.status_code == 200:
        response.raw.decode_content = True
        
        file_name = url.split("/")[-1]
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(response.raw, f)

        return file_name
    else:
        return None


def main():
    url = "https://apod.nasa.gov/apod/astropix.html"
    page = requests.get(url)
    if page.status_code != 200:
        print("Could not get APOD website. Status: {}".format(page.status_code))
        return

    soup = BeautifulSoup(page.text, 'html.parser')
    image = soup.find("img")
    image_link = "https://apod.nasa.gov/apod/" + image.parent.get('href')
    file_path = os.getcwd() + "\\" + download_image(image_link)
    if file_path is not None:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 0)
        time.sleep(5)
        os.remove(file_path)
    else:
        print("Error retreiving APOD Image.")

if __name__ == "__main__":
    main()
