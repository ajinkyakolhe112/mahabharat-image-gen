import os
from PIL import Image
import requests
import base64
from io import BytesIO

def is_image_file(filename):
    """Simple check for image file extensions"""
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))

def encode_image_to_base64(image):
    """Convert PIL Image to base64 string"""
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def generate_caption(image):
    """Generate caption using Ollama API"""
    base64_image = encode_image_to_base64(image)
    
    response = requests.post('http://localhost:11434/api/generate',
        json={
            'model': 'llava',
            'prompt': 'Describe this image',
            'images': [base64_image],
            'stream': False
        })
    
    return response.json()['response']

IMAGES_PATH = "mahabharat_images_dataset"

for subdirs in os.listdir(IMAGES_PATH):
    subdir_path = os.path.join(IMAGES_PATH, subdirs)
    if not os.path.isdir(subdir_path):
        print(f"Skipping {subdirs} - not a directory")
        continue
    
    for image_element in os.listdir(subdir_path):
        if not is_image_file(image_element):
            continue
            
        try:
            # Process image
            image_path = os.path.join(subdir_path, image_element)
            image = Image.open(image_path)
            caption = generate_caption(image)
            
            # Save caption
            txt_filename = os.path.splitext(image_element)[0] + '.txt'
            txt_path = os.path.join(subdir_path, txt_filename)
            with open(txt_path, 'w') as f:
                f.write(caption)
            
            print(f"Processed: {image_element}")
            
        except Exception as e:
            print(f"Error processing {image_element}: {str(e)}")