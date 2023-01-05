from sms.sms import Sms
from emailService.email import Email

def main():
    email = Email()
    m = email.send_message(email='mohamednaser1000.mn@gmail.com', title='Test', body='HelloWorld')
    print(m)

if __name__ == '__main__':
    main()
