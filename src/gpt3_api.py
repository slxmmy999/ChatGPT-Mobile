import openai
from api_keys import openai_apikey

openai.api_key = openai_apikey

messages=[
    {"role": "system", "content": "You are a helpful assistant. Users are interacting with you using their mobile messaging app. Please make sure your responses are mobile friendly and only in plain text. You are based on ChatGPT using the gpt-3.5-turbo model."}
]

model = "gpt-3.5-turbo"

def getOutput(input):
    messages.append({"role": "user", "content": input})

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    print(messages)

    bot_response = response.choices[0]["message"]["content"]
    messages.append({"role": "assistant", "content": bot_response})

    return bot_response