import smtplib
import os
from email.mime.text import MIMEText


def send_email():
    sender = "manager@vegaart.ru"
    password = "[eqnt,t"

    server = smtplib.SMTP("smtp.vegaart.ru", 587)
    server.starttls()

    try:
        with open("mail-from-commercial.html") as file:
            template = file.read()

    except IOError:
        return "The template was not found"

    
    try:
        server.login(sender, password)
        msg = MIMEText(template, "html")
        msg["From"] = sender
        msg["To"] = sender
        msg["Subject"] = "Коммерческое предложение"
        server.sendmail(sender, sender, msg.as_string())

        return "The message was send successfully!"
    
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password"

def main():
    print(send_email())

if __name__=="__main__":
    main()