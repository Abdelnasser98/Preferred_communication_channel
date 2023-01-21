from handlers_Interface import HandlerInterface
from emailService.email import Email


class Email_handler(HandlerInterface):
    @staticmethod
    def handler(email, message):
        email = Email()
        email.send_message(email=email, title='Automated Message', body=message)
