import json

from comChannelInterface import CommunicationChannel
from twilio.rest import Client


class Sms(CommunicationChannel):

    def __init__(self):
        creds = json.load(open('SMScreds.json'))
        account_sid = creds['AccountSID']
        account_auth = creds['AccountAuthToken']
        self.phoneNumber = creds['PhoneNumber']
        self.client = Client(account_sid, account_auth)

    def send_message(self, title=None, body='', number=None, email=None):
        message = self.client.messages.create(
            body=body,
            from_=self.phoneNumber,
            to=number
        )

        return message.sid
