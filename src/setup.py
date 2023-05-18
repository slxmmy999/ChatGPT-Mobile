#API Key from OpenAI
openai_apikey = "<your-key>"

# Phone number communications are sent to and from
phoneNumber = "<your-phone-number>"

# App specific password created in 2 Factor Auth tab in Google profile Security
gmail_password = "<your-password>"

# Email to be used with this project (It's recommended to create a new account specifically for this
# application to prevent clutter)
email = "<your-project-email>"


# List of carrier email endings. This does not need to be edited.
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

# Input the key from the dictionary above that responds to you carrier.
carrier = CARRIERS["<your-carrier>"]


# Whether logging is enabled or not
verbose = True