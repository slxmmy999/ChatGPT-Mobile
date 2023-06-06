import openai
from log import AppLogger

logger = AppLogger()

# Array of message history passed to model each time a response is requested
messages = [
    {"role": "system", "content": "You are a helpful assistant. Users are interacting with you using their mobile messaging app. Please make sure your responses are short and concise, mobile-friendly, and only in plain text. You are based on ChatGPT using the gpt-3.5-turbo model."}
]

# Model can be changed based on price and performance preferences, though 3.5-turbo is a very
# good middle ground between price and performance
model = "gpt-3.5-turbo"

def getOutput(input, key):
    openai.api_key = key
    try:
        messages.append({"role": "user", "content": input})

        logger.GPT_LOG_EVENT("Requesting ChatGPT response", "info")

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
           # max_tokens=300
        )

        # This makes sure the list of past messages is not too long and causing issues.
        # Zero research went in to this and I chose a random value so adjustent should
        # probably be made with further research
        if len(messages) > 30:
            logger.GPT_LOG_EVENT("Messages are over 30. Removing the first message.", "info")
            messages.pop(1)

        bot_response = response.choices[0]["message"]["content"]
        messages.append({"role": "assistant", "content": bot_response})

        logger.GPT_LOG_EVENT("ChatGPT response received", "info")

        return bot_response

    except openai.Error as e:
        # Handle OpenAI API errors
        logger.GPT_LOG_EVENT(f"OpenAI API error: {e}", "error")
        # Perform appropriate error handling or raise an exception

    except Exception as e:
        # Handle other exceptions
        logger.GPT_LOG_EVENT(f"Unexpected error: {e}", "error")
        # Perform appropriate error handling or raise an exception
