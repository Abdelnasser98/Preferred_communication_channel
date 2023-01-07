import csv


class ReadFile:
    @staticmethod
    def read_csv_file(return_type):
        preferredCom = []
        with open('csvFile.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if return_type == 'phone':
                    if row[2].__contains__("+"):
                        preferredCom.append(row[2])
                elif return_type == 'email':
                    preferredCom.append(row[1])

            print(preferredCom)
            return preferredCom
