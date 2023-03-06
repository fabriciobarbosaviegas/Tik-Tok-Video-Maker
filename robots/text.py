import openai
import os
from langdetect import detect



def write_script(key, theme):
    print("Writing video script...\n\n")

    messages = [
        {"role": "system", "content": "You are a useful assistant to help with all the processes involved in creating a video for TikTok"},
        {"role":"user", "content":f'Write a bullet Script from TikTok video about "{theme}" in {detect(theme)} language'}
        ]

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )


    response = completion.choices[0].message["content"]

    messages.append({"role":"system", "content":response})

    print(response)

    print(f"Sugested Keywords: {get_keywords(messages)}\n")    

    save_script(theme, response)

    return parse_text(response, theme)



def get_keywords(messages):
    messages.append({"role":"user", "content":"Get perfect keywords for this video"})
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    return completion.choices[0].message["content"]



def parse_text(text, theme):
    text = text.replace("\n", "")
    text = text.split("- ")[1:]
    text.insert(0, theme)

    return text



def save_script(theme, text):
    f = open(f"projects/scripts/{theme.replace(' ', '-')}.txt", "w")
    f.write(text)
    f.close()