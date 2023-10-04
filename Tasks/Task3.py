import smtplib
import time
import schedule
import urllib.request
from email.message import EmailMessage
from datetime import datetime

def read_csv(csv_file):
    data = []
    with open(csv_file, 'r') as f:
        # create a list of rows in the CSV file
        rows = f.readlines()

        # strip white-space and newlines
        rows = list(map(lambda x:x.strip(), rows))

        for row in rows:
            # further split each row into columns assuming delimiter is comma 
            row = row.split(',')

            # append to data-frame our new row-object with columns
            data.append(row)
    return data

def send_mail(
        to_email,
        subject,
        message,
        serverName='smtp.gmail.com',
        from_email='akshay.test.1001@gmail.com'
    ):

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(message)

    server = smtplib.SMTP(serverName, 25)
    server.ehlo()
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_email, 'keaw qufz yxsi jhpz')  # user & (app)password for 2fa
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')

def scheduleBirthdayWish():
    today = datetime.today().strftime('%Y-%m-%d')

    listOfEmails = read_csv('emails_list.csv')
    for row in listOfEmails:
        if (row[0] == 'Index'):
            continue

        dob = row[3]
        birthDate = datetime.strptime(dob, "%Y-%m-%d")
        todayDate = datetime.strptime(today, "%Y-%m-%d")

        if (birthDate.month == todayDate.month and birthDate.day == todayDate.day):
            email = row[1]
            content = 'Happy Birthday'

            send_mail(
                to_email=[email],
                subject='Birth day wishes',
                message = """
                %s
                """%(content)
            )

def is_connected():
    try:
        urllib.request.urlopen("https://www.example.com/", timeout=1)
        return True
    except urllib.request.URLError as err:
        return False

def main():
    print('Read the csv and send birthday email if today is their birthday')

    connection = is_connected()
    if (connection == False):
        print('Not connected to Internet')
        return

    schedule.every().day.at("00:00:00").do(scheduleBirthdayWish)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if (__name__ == '__main__'):
    main()
