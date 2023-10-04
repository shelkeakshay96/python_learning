import pywhatkit

def main():
    sendAtHour = 16
    sendAtMinuite = 39

    # Whatsweb must be logged in on default browser
    pywhatkit.sendwhatmsg("+919766209300", "HELLO AKSHAY!", sendAtHour, sendAtMinuite)

if (__name__ == '__main__'):
    main()
