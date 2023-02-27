# Tik Tok Video Maker
 Final Project from CS50
 
#### Video Demo:  <URL HERE>

## Description:

### The Project:

TikTok video maker is an application developed in python that uses a unique combination of several AIs and bots to generate completely original short videos in TikTok's own 4:3 format.

## Examples:

View examples in [@tiktokautovideomake](https://www.tiktok.com/@tiktokautovideomake) on TikTok.

## How to use:

To use TikTok Video Maker, you must have [python](https://www.python.org/) installed on your machine, as well as access to the Open Ai API.

#### Requirements:

To install the necessary python libraries run`pip install -r requiremnts.txt`.

#### How to get access to Open Ai api:

1. Create an account at [openai.com/api](https://openai.com/api)

![image](https://user-images.githubusercontent.com/49844765/221638788-0d6c8fbd-4290-45cc-8f23-a0dd698ec0de.png)

2. Then access "personal"

![image](https://user-images.githubusercontent.com/49844765/221639869-28a67f1f-ebdf-4645-9951-30f3a911117c.png)

3. And enter "View API key":

![image](https://user-images.githubusercontent.com/49844765/221640041-09c4cec8-e96c-48c1-ae60-d8f0837dd32f.png)

4. Create a new secret key and keep it in a safe place:

![image](https://user-images.githubusercontent.com/49844765/221640323-2c62ff80-7ac0-478a-9b08-b31b50c2d9cd.png)

#### Using the application:

Using the application is very simple, just run the "main.py" file and provide your open ai secret key and then define a theme for your video. After that, the video will start to be generated.

All generated files are available in folders inside the "projects" directory and can be accessed after the process.

## More details about the project:

### Bots:

#### text.py

This is the bot responsible for writing the video script and suggesting keywords for it. It does this through Open AI's "text-davinci-003" model, then the generated text is saved and returned to the main file.

#### images.py

This bot is responsible for generating, adjusting and subtitling the images for the video, based on the generating script. It uses Open Ai's "DALL-E" template for this.

* First the bot receives the script line by line as prompts and generates the images in 500x500 (due to A.I limitations).
* These images are then reconverted to 720x1280 format using the Pillow library in python and subtitled.
* These images are then saved in your folder in the "projects" directory and the program continues to run.

#### audio.py

This bot uses the python gTTs library to synthesize script lines into audio files that are unified and saved in the projects directory.

#### video.py:

This is the bot responsible for making all the magic possible, it uses the openCV library to concatenate all the images generated into a single video, using the previously generated audios as time limiters that each image can stay on screen. It then merges the unified audio with the generated video and exits the program.

The final result is saved inside its respective folder in the projects directory.
