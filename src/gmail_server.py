from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import time
import base64
from sms_api import MessageService
from bs4 import BeautifulSoup
from gpt3_api import getOutput
from setup import phoneNumber, carrier
from log import AppLogger

logger = AppLogger()
ms = MessageService()
logger.GMAIL_LOG_EVENT("NEW RUN STARTED", "info")

# Set up OAuth2 credentials flow
# You must obtain the proper credentials from the Google Developer Portal
flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify'],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob'
)

# Perform OAuth2 authorization
credentials = flow.run_local_server()
logger.GMAIL_LOG_EVENT("Auth server completed", "info")
service = build('gmail', 'v1', credentials=credentials)

def handle_new_message(message):
    # Get the message ID
    message_id = message['id']

    # Retrieve the full message using the ID
    full_message = service.users().messages().get(userId='me', id=message_id).execute()

    # Extract the message content
    sender = extract_sender(full_message)

    # Only respond to emails from the known sender
    if sender == phoneNumber + carrier:
        message_content = extract_message_content(full_message)

        # Process the new message (e.g., print message content)
        response = getOutput(message_content)
        ms.send_message(phoneNumber, response)
    mark_message_as_read(message_id)

# Mark message as read so they are not responded to more than once
def mark_message_as_read(message_id):
    service.users().messages().modify(
        userId='me',
        id=message_id,
        body={
            'removeLabelIds': ['UNREAD']
        }
    ).execute()

def extract_sender(message):
    headers = message['payload'].get('headers', [])
    for header in headers:
        if header['name'] == 'From':
            return header['value']
    logger.GMAIL_LOG_EVENT("Could not find sender", "warning")
    return ''


# TODO: This code assumes all carriers send the data in the same way. This must be tested with
# each carrier. This method is working with AT&T but has not been tested with other carriers.
def extract_message_content(message):
    payload = message.get('payload')
    parts = payload.get('parts')
    data = None

    for part in parts:
        nested_parts = part.get("parts")
        lowest = ""
        while nested_parts:
            lowest = nested_parts[0]
            nested_parts = nested_parts[0].get("parts")
        data = lowest['body'].get('data')

    if data:
        message_data = base64.urlsafe_b64decode(data).decode('utf-8')
        soup = BeautifulSoup(message_data, 'html.parser')
        td_tag = soup.find('td')

        if td_tag:
            content = td_tag.get_text(strip=True)
        else:
            logger.GMAIL_LOG_EVENT("Could not find <td> tag", "error")
        return content
    logger.GMAIL_LOG_EVENT("Could not find message content", "warning")
    return ''

def poll_new_messages():
    logger.GMAIL_LOG_EVENT("POLLING FOR MESSAGES", "info")
    while True:
        # Poll for new messages
        try:
            response = service.users().messages().list(
                userId='me',
                q='is:unread'
            ).execute()

            unread_messages = response.get('messages', [])

            # Process the new message event
            if unread_messages:
                logger.GMAIL_LOG_EVENT("New message recieved, extracting content", "info")
                # Handle new message(s) as needed
                handle_new_message(unread_messages[0])
        except Exception as e:
            # Handling the exception
            logger.GMAIL_LOG_EVENT(f"Exception: {e}", "error")

        # Wait for a specific interval before polling again
        time.sleep(1)  # Adjust the interval as needed

# Start polling for new messages
poll_new_messages()