import cv2
import numpy as np
import os
from mutagen.mp3 import MP3
from moviepy.editor import *



def generate_video(path, theme):
    print("Generating video...\n")

    if not os.path.exists(path.replace("images", "videos")):
        os.mkdir(path.replace("images", "videos"))
    create_video(path, theme)

    print("Adding audio from video...\n")
    
    videoclip = add_audio_to_video(f"../../audios/{theme}", theme)

    print("Saving video...")

    videoclip.write_videofile(f"../../videos/{theme}/{theme}.mp4")



def create_video(path, theme):
    image_folder = f'../../images/{theme}'
    video_name = f"{theme}-mute.avi"
    os.chdir(path.replace("images", "videos"))
    images = []
    
    for img in os.listdir(image_folder):
        if img.endswith(".jpg"):
            for i in range(frame_size(img.replace('.jpg', ''), f"../../audios/{theme}")):
                images.append(img)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX') 

    frame = cv2.imread(os.path.join(image_folder, images[0]))
 
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder,image)))
         
    cv2.destroyAllWindows()
    video.release()



def frame_size(frame, path):
    audio = MP3(f"{path}/{frame}.mp3")
    return round(audio.info.length)



def add_audio_to_video(path, theme):
    clip = VideoFileClip(f"{path.replace('audios', 'videos')}/{theme}-mute.avi")
    audioclip = AudioFileClip(f"{path}/final.mp3")

    return clip.set_audio(audioclip)