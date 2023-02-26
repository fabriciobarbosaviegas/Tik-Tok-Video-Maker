from credentials.init import init_credentials
from robots.text import write_script
from robots.image import generate_image
from robots.audio import generate_audio
import os


def main():
    api_key = input("Open AI Api Key:")
    theme = input("Video Theme: ")

    init_credentials(api_key)

    script = write_script(api_key, theme)

    try:
        cleanPath(f"projects/images/{theme.replace(' ', '-')}")
        cleanPath(f"projects/audios/{theme.replace(' ', '-')}")
    except:
        pass
    
    generate_video_assets(script, theme)



def generate_video_assets(prompts, theme):
    for prompt in prompts:
        generate_image(prompt, theme)
        generate_audio(prompt, theme)


def cleanPath(path):

   for filename in os.listdir(path):

       file_path = os.path.join(path, filename)

       try:
           if os.path.isfile(file_path) or os.path.islink(file_path):
               os.unlink(file_path)

       except Exception as e:
           print('Failed to delete %s. Reason: %s' % (file_path, e))



if __name__ == "__main__":
    main()