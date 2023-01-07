
from sms.sms import Sms
from emailService.email import Email


class ComFactory:

    def channel(channel):
        sms = Sms()
        emailService = Email()
        if channel == 'SMS':
            number = input('Please Enter the number you are messaging..!')
            message = input('Your message:\t')
            res = sms.send_message(number=number, body=message)
            print(res)
            return True
        elif channel == 'Email':
            email = input(
                'Please enter the email address you are emailling..!\t')
            title = input('Please enter the title of your email..!\t')
            body = input('Your message:\t')
            res = emailService.send_message(
                email=email, title=title, body=body)
            print(res)
            return True
        else:
            raise Exception(
                TypeError(channel + 'This service is undefined...'))
