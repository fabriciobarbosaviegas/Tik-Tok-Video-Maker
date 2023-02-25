import openai

def write_script(key, theme):
    openai.api_key = key

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
    return parse_text(response)



def parse_text(text):
    text = text.replace("\n", "")
    return text.split("• ")[1:]