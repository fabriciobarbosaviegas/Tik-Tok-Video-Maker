import openai
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os
import requests
from utils import get_file_number
from unidecode import unidecode
import re
import math



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

            save_image(image_content, theme, prompt)

            print(f"Generated Image: {image_content}\n")

            break
        
        except Exception as e:
            print(f"Error to generate image from prompt:{e}.\nTrys: ({trys+1}/3)\nTrying again...")

        if trys+1 == 3:
            print(f"Image not generated!\n")



def save_image(image, theme, text):
    adjusted_image = adjust_image(image, text)

    path = os.path.join("projects/images", unidecode(theme.replace(' ', '-')))
    
    if not os.path.exists(path):
        os.mkdir(path)


    adjusted_image.save(f"{path}/{get_file_number(path)}.jpg", "JPEG")



def adjust_image(image, text):
    background_image, draw = create_background_image(image)
    insert_image(background_image, image)
    insert_subtitles(draw, text)

    return background_image



def create_background_image(image):
    background_image = Image.open(requests.get(image, stream=True).raw).resize((720,1280)).filter(ImageFilter.GaussianBlur(5))

    draw = ImageDraw.Draw(background_image)

    return background_image, draw



def insert_image(background_image, image):
    insert_image_content = Image.open(requests.get(image, stream=True).raw).convert("RGBA")

    insert_image_x = round((720 - 500) / 2)
    insert_image_y = 320

    background_image.paste(insert_image_content, (insert_image_x, insert_image_y), insert_image_content)



def insert_subtitles(draw, text):
    font = ImageFont.truetype("projects/fonts/ComicNeue-BoldItalic.ttf", 40)
    text = addBreakLines(text)

    text_width, text_height = draw.textsize(text, font=font)

    print(text_width)

    x = round((720 - text_width) / 2)
    draw.multiline_text((x, 898), text, font=font, fill="black", align="center")
    draw.multiline_text((x, 900), text, font=font, fill="yellow", align="center")



def addBreakLines(text, limit=20):

    index = getAllIndicesOf(" ", text)
    correctSpaces = ""
    c = 1

    if len(text) > limit:

        for i in range(math.ceil(len(text)/limit) - 1):

            for j in range(len(index)):

                if index[j] >= limit * c and i <= round(len(text)/limit):

                    correctSpaces = index[j-1]
                    break

            c += 1

            try:
                text = text[:correctSpaces] + "\n" + text[correctSpaces:]
            except:
                pass
            
            index = getAllIndicesOf(" ", text)

        if text.find('\n\n') > 0:
            text = text.replace('\n\n', '\n')

        return text

    else:
        return text
    


def getAllIndicesOf(search, searchString):
    return [m.start() for m in re.finditer(search, searchString)]