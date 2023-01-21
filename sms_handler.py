from handlers_Interface import HandlerInterface
from sms.sms import Sms
class Sms_handler(HandlerInterface):
    @staticmethod
    def handler(sms_numbers:list, message:str):
        sms = Sms()
        for number in sms_numbers:
            sms.send_message(body=message, number=number)
