import getpass
import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def send(recip='Tim Head <thead@cern.ch>',
         sender='Tim Head <thead@cern.ch>'):
    email_text = """Hello all,

it will be Thursday soon! Go cycling:

Thursday, 6pm, Gate C.

We wait for everyone. Bring your own puncture repair kit. Don't forget to bring your bike!

T
ps. this will be the best ride ever!
"""
    message = MIMEText(email_text)
    message['From'] = sender
    message['Subject'] = "Velo Thursday"
    message['To'] = recip
    
    send_to = [recip]

    cyclists = open("cyclists.txt").readlines()
    message["Cc"] = ", ".join(cyclists)
    send_to += cyclists

    # Now send the message
    username = 'thead'
    password = getpass.getpass("SMTP server password: ")
    
    s = smtplib.SMTP('smtp.cern.ch', port=587)
    try:
        s.ehlo()
        if s.has_extn("STARTTLS"):
            s.starttls()
            # have to re-identify after starting TLS
            s.ehlo()

        s.login(username, password)

        s.sendmail(sender, send_to, message.as_string())

    finally:
        s.quit()


if __name__ == "__main__":
    send()
