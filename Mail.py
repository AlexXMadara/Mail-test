import requests

# Function to get a temporary email address
def get_temp_email():
    response = requests.get('https://api.temp-mail.org/request/mail/id/1')
    if response.status_code == 200:
        return response.json()['email']
    else:
        print("Error fetching temp email")
        return None

# Function to check for incoming emails
def check_incoming_emails(email):
    response = requests.get(f'https://api.temp-mail.org/request/mail/id/{email}')
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching emails")
        return None

# Example usage
temp_email = get_temp_email()
if temp_email:
    print(f'Temporary email: {temp_email}')
    # Add further processing, like sending verification emails or checking for received emails
