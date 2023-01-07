from comFactory import ComFactory


def main():
    """Execution of the main function -- clientSide"""
    program_on = True

    while program_on:
        channel = input("please Select your prefered channel..")
        factory = ComFactory.channel(channel=channel)
        if factory:
            program_on = False


if __name__ == '__main__':
    main()
