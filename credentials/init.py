import openai

def init_credentials(openai_key):
    openai_init(openai_key)



def openai_init(key):
    openai.api_key = key
