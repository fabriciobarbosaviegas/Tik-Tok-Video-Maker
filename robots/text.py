import openai
import os

def write_script(key, theme):
    print("Writing video script...\n\n")

    model_engine = "text-davinci-003"
    prompt = f'Write a bullet Script from TikTok video about "{theme}"'

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text

    save_script(theme, response)

    return parse_text(response, theme)



def parse_text(text, theme):
    text = text.replace("\n", "")
    text = text.split("• ")[1:]
    text.insert(0, theme)

    return text



def save_script(theme, text):
    f = open(f"projects/scripts/{theme.replace(' ', '-')}.txt", "w")
    f.write(text)
    f.close()