import random
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create():
    while True:
        placeholder = random.randint(0, 5)
        key = random.randint(0, 9)
        if placeholder != key:
            return placeholder * 10 + key


class Token:

    def __init__(self):
        self.message_template_path = "assets/email_body_"
        self.msg_id = 'cls6789678'

    @staticmethod
    def generate_otp(length=6):
        otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        return otp

    def settemplate(self, id_input):
        self.msg_id = id_input
        self.message_template_path = self.message_template_path + self.msg_id + '.html'

    def format_message(self, otp):
        message_path = self.message_template_path
        with open(message_path, 'r') as html_file:
            html_file_content = html_file.read().replace(self.msg_id, str(otp))

        html_content = html_file_content
        html_part = MIMEText(html_content, "html")
        message = MIMEMultipart("alternative")
        message.attach(html_part)
        message["subject"] = "Verification"
        return message

    def send_mail(self, otp, recipient_email):
        sender_email = "snowwing14@gmail.com"
        password = "nsxw xpoo rnup cwzs"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, self.format_message(otp).as_string())


def verify(recipient_email, token):
    placeholder = token // 10
    key = token % 10
    temp_obj = Token()
    otp = temp_obj.generate_otp(5)
    temp_obj.settemplate('cls6789678')
    temp_obj.send_mail(otp, recipient_email)

    entered_otp = input("Enter the OTP you received: ")

    modified_otp = otp[:placeholder] + str(key) + otp[placeholder:]

    if entered_otp == modified_otp:
        print("Authentication successful!")
        return True
    else:
        print("Invalid OTP. Authentication failed.")
        return False
