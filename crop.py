from PIL import Image
import os
import requests
from io import BytesIO

def crop_image(input_path, output_path):
    with Image.open(input_path) as img:
        # Définir les coordonnées de recadrage
        left = 30
        top = 30
        right = img.width - 30
        bottom = img.height - 298
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception(f"Failed to download image from {url}")

def batch_crop_images(image_urls, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for url in image_urls:
        try:
            img = download_image(url)
            filename = os.path.basename(url)
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)  # Sauvegarder l'image téléchargée
            crop_image(output_path, output_path)  # Recadrer l'image
        except Exception as e:
            print(f"Error processing {url}: {e}")

# Exemple d'utilisation
image_urls = [
    'https://www.delightlamps.com/cdn/shop/files/54_3f2570ea-a02c-4089-8b70-589d5fcec80a.png',
    'https://www.delightlamps.com/cdn/shop/files/56_3e441159-3c45-4896-b236-5d2e927d69ad.png',
    'https://www.delightlamps.com/cdn/shop/files/67_14d9b84f-17cd-47a8-8d96-c3a0f289d23e.png',
    'https://www.delightlamps.com/cdn/shop/files/66_ee6f9c86-8f51-4202-84be-d83a47bf4c7c.png',
    'https://www.delightlamps.com/cdn/shop/files/64_a5da1415-5dfb-4fee-8778-c7567b9bf294.png'
    # Ajoutez d'autres URLs d'images ici
]
output_folder = 'images/output'
batch_crop_images(image_urls, output_folder)