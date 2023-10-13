import smtplib
from sys import *
import smtplib
import urllib.error
import urllib.request
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

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
    server.starttls()
    server.login(from_email, 'keaw qufz yxsi jhpz')  # user & (app)password for 2fa
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail to', to_email)

def is_connected():
    try:
        urllib.request.urlopen("https://www.example.com/", timeout=1)
        return True
    except urllib.request.URLError as err:
        return False

def send_mail_with_attachment(toaddr, subject, body, filename):
    if (is_connected() == False):
        print ("Not connected to network.")
        return
    try:
        fromaddr = "akshay.test.1001@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
    
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr,"keaw qufz yxsi jhpz")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        print("Log file successfully sent through Mail")
            
    except Exception as E:
        print ("Unable to send mail.",E)