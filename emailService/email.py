import os.path
import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from factory_method.comChannelInterface import CommunicationChannel


class Email(CommunicationChannel):

    def __init__(self):
        self.creds = None
        SCOPES = ['https://mail.google.com/',
                  "https://www.googleapis.com/auth/gmail.send"]
        if os.path.exists('../token.json'):
            self.creds = Credentials.from_authorized_user_file(
                'token.json', SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    r'D:\python\prefCommunicationChannels\emailService\credentials.json', SCOPES
                )
                self.creds = flow.run_local_server(port=0)
                with open('token.json', 'w') as token:
                    token.write(self.creds.to_json())

    def send_message(self, title=None, body='', email=None):
        try:
            service = build('gmail', 'v1', credentials=self.creds)
            message = EmailMessage()
            message.set_content(body)

            message['To'] = email
            message['From'] = ''
            message['Subject'] = title

            encoded_message = base64.urlsafe_b64encode(
                message.as_bytes()).decode()
            create_message = {
                'raw': encoded_message
            }
            send_message = (service.users().messages().send(
                userId='me', body=create_message).execute())
        except HttpError as error:
            print(error)
            send_message = None
        return send_message
