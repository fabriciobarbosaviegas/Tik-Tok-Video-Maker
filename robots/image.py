import openai
from PIL import Image, ImageDraw, ImageFilter
import os
import requests
from utils import get_file_number



def generate_image(prompt, theme=''):
    print('Generating images from script prompts...\n')

    print(f'Prompt: {prompt}')

    for trys in range(3):
        try:
            response = openai.Image.create(
                prompt=prompt,
                n = 1,
                size = "512x512"
            )

            image_content = response['data'][0]['url']

            save_image(image_content, theme)

            print(f"Generated Image: {image_content}\n")

            break
        
        except Exception as e:
            print(f"Error to generate image from prompt:{e}.\nTrys: ({trys+1}/3)\nTrying again...")

        if trys+1 == 3:
            print(f"Image not generated!\n")



def save_image(image, theme):
    adjusted_image = adjust_image(image)

    path = os.path.join("projects/images", theme.replace(' ', '-'))
    
    if not os.path.exists(path):
        os.mkdir(path)


    adjusted_image.save(f"{path}/{get_file_number(path)}.jpg", "JPEG")



def adjust_image(image):
    background_image = create_background_image(image)
    insert_image(background_image, image)

    return background_image



def create_background_image(image):
    background_image = Image.open(requests.get(image, stream=True).raw).resize((720,1280)).filter(ImageFilter.GaussianBlur(5))

    draw = ImageDraw.Draw(background_image)

    return background_image



def insert_image(background_image, image):
    insert_image_content = Image.open(requests.get(image, stream=True).raw).convert("RGBA")

    insert_image_x = round((720 - 500) / 2)
    insert_image_y = 320

    background_image.paste(insert_image_content, (insert_image_x, insert_image_y), insert_image_content)