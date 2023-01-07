import csv


class ReadFile:
    def read_csv_file(self):
        preferredCom = {}
        with open('csvFile.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row.__contains__('email'):
                    preferredCom[row[0]] = row[1]
                else:
                    preferredCom[row[0]] = row[2]

        print(preferredCom)


rf = ReadFile()
rf.read_csv_file()
