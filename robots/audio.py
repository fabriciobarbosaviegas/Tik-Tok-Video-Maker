from gtts import gTTS
import os
from langdetect import detect
from utils import get_file_number
from unidecode import unidecode
from pydub import AudioSegment



def generate_audio(text, theme):
    audio = gTTS(text=text, lang=detect(text), slow=False)

    path = os.path.join("projects/audios", unidecode(theme.replace(' ', '-')))

    if not os.path.exists(path):
        os.mkdir(path)

    audio.save(f"{path}/{get_file_number(path)}.mp3")



def merge_audios(path):
    audios = []

    for audio in os.listdir(path):
        if audio.endswith(".mp3"):
            audios.append(AudioSegment.from_mp3(f"{path}/{audio}"))

    combined = audios[0]

    for i in audios[1:]:
        combined += i

    combined.export(f"{path}/final.mp3", format="mp3")