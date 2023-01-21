import csv
from threading import Thread
from sms_handler import Sms_handler
from email_handler import Email_handler

class ReadFile:
    @staticmethod
    def read_csv_file(file_path:str):
        email_address = []
        sms_numbers = []
        with open(file_path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["email address"] or row["email"] or row["emails"]:
                    email_address.append(row["email address"] or row["email"] or row["emails"])
                if row["phone number"] or row["phone"] or row["sms"]:
                        if row["phone number"] != 'null':
                            sms_numbers.append(row["phone number"] or row["phone"] or row["sms"])
                        else:
                            continue
        sms_thread = Thread(target=Sms_handler.handler(sms_numbers,message="test"))
        email_thread = Thread(target=Email_handler.handler(email_address,message="test"))
        """""""Starting multiple threads"""""""
        sms_thread.start()
        email_thread.start()
        """"Joining the threads together after finishing the function"""""
        sms_thread.join()
        email_thread.join()



rf = ReadFile
rf.read_csv_file(file_path='D:\python\prefCommunicationChannels/csvFile.csv')