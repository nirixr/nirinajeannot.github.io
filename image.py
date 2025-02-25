from PIL import Image
import os

def crop_image(input_path, output_path):
    with Image.open(input_path) as img:
        # Définir les coordonnées de recadrage
        left = 17
        top = 900-17
        right = 600-17
        bottom = 900 - 298  # 900 est la hauteur totale de l'image
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)

def batch_crop_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            crop_image(input_path, output_path)

# Exemple d'utilisation
input_folder = 'images/input'
output_folder = 'images/output'
batch_crop_images(input_folder, output_folder)