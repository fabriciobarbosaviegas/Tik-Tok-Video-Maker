from credentials.init import init_credentials
from robots.text import write_script
from robots.image import generate_image
from robots.audio import generate_audio, merge_audios
from robots.video import generate_video
from unidecode import unidecode
import os
from utils import cleanAllPaths



def main():
    api_key = input("Open AI Api Key:")
    theme = input("Video Theme: ")

    init_credentials(api_key)

    cleanAllPaths(theme)

    script = write_script(api_key, theme)

    generate_video_assets(script, theme)

    merge_audios(f"projects/audios/{unidecode(theme.replace(' ', '-'))}")

    generate_video(f"projects/images/{unidecode(theme.replace(' ', '-'))}", unidecode(theme.replace(' ', '-')))



def generate_video_assets(prompts, theme):
    for prompt in prompts:
        generate_image(prompt, theme)
        generate_audio(prompt, theme)



if __name__ == "__main__":
    main()