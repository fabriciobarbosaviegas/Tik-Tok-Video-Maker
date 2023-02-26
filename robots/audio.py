from gtts import gTTS
import os
from langdetect import detect
from utils import get_file_number



def generate_audio(text, theme):
    audio = gTTS(text=text, lang=detect(text), slow=False)

    path = os.path.join("projects/audios", theme.replace(' ', '-'))

    if not os.path.exists(path):
        os.mkdir(path)

    audio.save(f"{path}/{get_file_number(path)}.mp3")