import openai
from setup import openai_apikey
from log import AppLogger

logger = AppLogger()

openai.api_key = openai_apikey

messages=[
    {"role": "system", "content": "You are a helpful assistant. Users are interacting with you using their mobile messaging app. Please make sure your responses are mobile friendly and only in plain text. You are based on ChatGPT using the gpt-3.5-turbo model."}
]

model = "gpt-3.5-turbo"

def getOutput(input):
    messages.append({"role": "user", "content": input})

    logger.GPT_LOG_EVENT("Requesting ChatGPT response", "info")

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    if len(messages) > 30:
        logger.GPT_LOG_EVENT("Messages are over 30. Removing first message.", "info")
        messages.pop(1)

    bot_response = response.choices[0]["message"]["content"]
    messages.append({"role": "assistant", "content": bot_response})

    logger.GPT_LOG_EVENT("ChatGPT response recieved", "info")

    return bot_response