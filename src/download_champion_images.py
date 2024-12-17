import os
import requests
from bs4 import BeautifulSoup

URL = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
SAVE_DIR = "champion_images"

os.makedirs(SAVE_DIR, exist_ok=True)

def download_champion_images():
    response = requests.get(URL)
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.select("table tbody tr td div.floatleft a img")

    for img in images:
        img_url = img.get("data-src") or img.get("src")
        img_name = img.get("data-image-name") or os.path.basename(img_url)

        if img_url and img_name:
            save_path = os.path.join(SAVE_DIR, img_name)
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                
                with open(save_path, "wb") as file:
                    file.write(img_response.content)
                
                print(f"다운로드 완료: {img_name}")
            except Exception as e:
                print(f"{img_name} 이미지 다운로드 실패: {e}")

if __name__ == "__main__":
    download_champion_images()
