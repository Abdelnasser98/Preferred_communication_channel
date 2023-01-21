from comFactory import ComFactory
from readingFiles import ReadFile

def main():
    """Execution of the main function -- clientSide"""
    program_on = True

    while program_on:
        file_path = input("please Select your prefered channel..")
        reading_files = ReadFile.read_csv_file(file_path=file_path)
        # if factory:
        #     program_on = False


if __name__ == '__main__':
    main()
