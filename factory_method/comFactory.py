
from sms.sms import Sms
from emailService.email import Email
from readingFiles import ReadFile


class ComFactory:
    @staticmethod
    def channel(channel):

        if channel == 'SMS':
            sms = Sms()
            rf = ReadFile.read_csv_file('phone')
            message = input('Your message:\t')
            for number in rf:
                res = sms.send_message(number=number, body=message)
                print(res)
            return True
        elif channel == 'Email':
            emailService = Email()
            rf = ReadFile.read_csv_file('email')
            title = input('Please enter the title of your email..!\t')
            body = input('Your message:\t')
            for email in rf:
                res = emailService.send_message(
                email=email, title=title, body=body)
                print(res)
            return True
        else:
            raise Exception(
                TypeError(channel + 'This service is undefined...'))
