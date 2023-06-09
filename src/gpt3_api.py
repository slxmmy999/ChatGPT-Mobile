import openai
from log import AppLogger

logger = AppLogger()

system_message = {"role": "system", "content": "Please follow these guidelines strictly! You are a helpful assistant. Please make sure your responses are SHORT and CONCISE, mobile-friendly, and only in plain text. You are based on ChatGPT using the gpt-3.5-turbo model."}

# Array of message history passed to model each time a response is requested
messages = [
    system_message
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
        if len(messages) > 10:
            logger.GPT_LOG_EVENT("Messages are over 10. Removing the first message.", "info")
            messages.pop(0)
            # bot forgets to send short messages so it must be reminded. This is important 
            # because the API will take up to 30 seconds to respond if the message is too long
            if not system_message in messages:
                messages.append(system_message)
                logger.GPT_LOG_EVENT("System message added to messages again", "info")

        bot_response = response.choices[0]["message"]["content"]
        messages.append({"role": "assistant", "content": bot_response})

        logger.GPT_LOG_EVENT("ChatGPT response received", "info")

        return bot_response

    except openai.OpenAIError as e:
        # Handle OpenAI API errors
        logger.GPT_LOG_EVENT(f"OpenAI API error: {e}", "error")
        # Perform appropriate error handling or raise an exception

    except Exception as e:
        # Handle other exceptions
        logger.GPT_LOG_EVENT(f"Unexpected error: {e}", "error")
        # Perform appropriate error handling or raise an exception
