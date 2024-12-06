import os
from PIL import Image
from lmdeploy import pipeline, ChatTemplateConfig

def is_image_file(filename):
    """Simple check for image file extensions"""
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))

# Initialize model
pipe = pipeline('xtuner/llava-llama-3-8b-v1_1-hf',
                chat_template_config=ChatTemplateConfig(model_name='llama3'))

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
            image      = Image.open(image_path)
            response   = pipe(('describe this image', image))
            
            # Save caption
            txt_filename = os.path.splitext(image_element)[0] + '.txt'
            txt_path     = os.path.join(subdir_path, txt_filename)
            with open(txt_path, 'w') as f:
                f.write(subdirs + ".\t" +response.text)
            
            print(f"Processed: {image_element}")
            
        except Exception as e:
            print(f"Error processing {image_element}: {str(e)}")