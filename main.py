from readingFiles import ReadFile

def main():
    """Execution of the main function -- clientSide"""
    program_on = True

    while program_on:
        file_path = input("please Select your prefered channel..")
        message = input("Write your message!")
        reading_files = ReadFile.read_csv_file(file_path=file_path, message=message)
        program_on = reading_files


if __name__ == '__main__':
    main()
