import os
import json
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    """
    :return: gets the service token (copied from online docs)
    """
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


def get_unread_emails(service):
    """
    :param google service:
    :return gets number of unread emails:
    """
    results = service.users().messages().list(
        userId='me',
        q='is:unread'
    ).execute()

    messages = results.get('messages', [])
    return len(messages)

def get_emails_today(service):
    """
    :param service:
    :return gets number of emails per day:
    """
    today = datetime.now().strftime("%Y/%m/%d")

    query = f"after:{today}"

    results = service.users().messages().list(
        userId='me',
        q=query
    ).execute()

    messages = results.get('messages', [])
    return len(messages)


def update_json(unread_emails, emails):
    filepath = "current_stress.json"

    with open(filepath, "r") as f:
        data = json.load(f)

    data["unread_emails"] = unread_emails
    data["emails"] = emails

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Updated emails to {emails}")
    print(f"Updated unread emails to {unread_emails}")


def main():
    service = get_gmail_service()
    unread_emails = get_unread_emails(service)
    emails = get_emails_today(service)
    update_json(unread_emails, emails)


if __name__ == "__main__":
    main()