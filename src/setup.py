# clear the terminal
def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# check if the user has a valid OpenAI API key
def validate_apikey(apikey: str) -> bool:
    import openai
    openai.api_key = apikey
    try:
        openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "This is a test message"}],
            max_tokens=1
        )
        return True
    except Exception as e:
        print(e)
        return False
    
# get the user's OpenAI API key
def get_openai_apikey(retry: bool = False):
    if retry:
        openai_apikey = input("Your OpenAI API key was invalid. Please try again: ")
    else:
        openai_apikey = input("Please enter your OpenAI API key: ")
    if validate_apikey(openai_apikey):
        return openai_apikey
    else:
        return get_openai_apikey(True)

# get the user's email address
def get_email(retry: bool = False):
    if retry:
        email = input("Your email address was invalid. Please try again: ")
    else:
        email = input("Please enter the Gmail address you are using for this application: ")
    if "@" in email and "." in email:
        return email
    else:
        return get_email(True)
    
# get the user's Gmail app specific password
def get_gmail_password(retry: bool = False):
    if retry:
        gmail_password = input("Your Gmail app specific password was invalid. Please try again: ")
    else:
        gmail_password = input("Please enter the Gmail app specific password you are using for this application: ")
    if len(gmail_password) == 16:
        return gmail_password
    else:
        return get_gmail_password(True)
    
# get the user's phone number
def get_phone_number(retry: bool = False):
    if retry:
        phoneNumber = input("Your phone number was invalid. Please try again: ")
    else:
        phoneNumber = input("Please enter the phone number you are using for this application (no spaces or dashes): ")
    if len(phoneNumber) == 10 and phoneNumber.isnumeric():
        return phoneNumber
    else:
        return get_phone_number(True)
    
# get the user's carrier
def get_carrier(retry: bool = False):
    carriers = ["att", "tmobile", "verizon", "sprint"]
    if retry:
        carrier = input("Your carrier was invalid. Please try again (type -ls for a list of carriers): ")
    else:
        carrier = input("Please enter your carrier (type -ls for a list of carriers): ")
    if carrier in carriers:
        return carrier
    elif carrier == "-ls":
        carriers = """
        att
        tmobile
        verizon
        sprint
        """
        print(carriers)
        return get_carrier()
    else:
        return get_carrier(True)

if __name__ == "__main__":
    welcome_message = """
    Thank you for using ChatGPT-Mobile! This is a proof of concept and is not intended for production use.
    This project is still under development and we welcome any contributions. Please see the README for more information.

    You will be asked to provide some information to get started. This information will be stored in a file called `.env` in the root directory of this project.
    We do not store any API keys or app specific passwords and all sensitive information remains on your machine.

    Please read the README for more information about this project and how to get started, and feel free to create an issue if you have any questions or concerns.

    Press enter to continue...
    """

    print(welcome_message)

    # wait for the user to press enter
    key = input()
    while key != "":
        key = input()

    clear()


    openai_apikey = get_openai_apikey()
    email = get_email()
    gmail_password = get_gmail_password()
    phoneNumber = get_phone_number()
    carrier = get_carrier()

    env_file = ".env"

    env_variables = {
        "openai_apikey": openai_apikey,
        "email": email,
        "gmail_password": gmail_password,
        "phoneNumber": phoneNumber,
        "carrier": carrier,
        "verbose": True
    }

    # write the environment variables to the .env file  
    with open(env_file, "w") as f:
        for key, value in env_variables.items():
            f.write(f"{key}={value}\n")

    print("Setup complete! Please see the README for more information about how to run this application.")