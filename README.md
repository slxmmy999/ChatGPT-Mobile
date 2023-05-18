# ChatGPT-Mobile

ChatGPT-Mobile is a project that enables users to utilize their phone's built-in MMS messaging application as a client to interact with ChatGPT, an AI language model developed by OpenAI. With this project, users can have conversations with ChatGPT by sending MMS messages from their mobile devices.

This README will guide you through the setup and usage of the ChatGPT-Mobile project, allowing you to quickly get started with using ChatGPT through MMS.
## Features

- **MMS-based Interaction**: Engage in natural language conversations with ChatGPT using MMS messages sent from your phone's built-in messaging app.
- **Text-to-Text Conversations**: Send text messages to ChatGPT and receive responses as MMS messages on your phone.
- **Conversational AI**: Utilize the power of ChatGPT, a state-of-the-art language model, to have meaningful and context-aware conversations.

<img src="https://github.com/slxmmy999/ChatGPT-Mobile/assets/62761327/60a815a0-2334-44ce-a8b0-8043b7f9ccf8" alt="Image" width="300">

## Setup

1. Clone the repository:
```
git clone https://github.com/slxmmy999/ChatGPT-Mobile.git
```

2. Install the required Python dependencies. Open a terminal or command prompt, navigate to the project directory, and run the following command:
```
pip install -r requirements.txt
```

3. Acquire Gmail OAuth `credentials.json` file from the Google Cloud Console and place the file in the root folder of the repository.

4. Create an application specific password for Gmail and use it to define the variable `gmail_password` in `setup.py`

5. Define the rest of the variables in `setup.py`

6. Run:
```
python src/gmail_server.py
```

7. Send an MMS message to the email being used for this application. Functionality is currently very slow so it may take a while to recieve a response.

## Contributions

I am open to all collaborators and ANY contributions are welcome, whether it's knowledge, hardware, or code. Please feel free to send me a message on any platform with whatever proposal you may have and I will get back to you as soon as possible.
