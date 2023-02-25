from credentials.init import init_credentials
from robots.text import write_script
from robots.image import generate_image
import os


def main():
    api_key = input("Open AI Api Key:")
    theme = input("Video Theme: ")

    init_credentials(api_key)

    script = write_script(api_key, theme)

    path = os.path.join("projects/images", theme.replace(' ', '-'))
    
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        cleanPath(path)

    generate_images(script, theme)



def generate_images(prompts, theme):
    for prompt in prompts:
        generate_image(prompt, theme)


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