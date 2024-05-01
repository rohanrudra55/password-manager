import random
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Token:

    def __init__(self):
        self.message_template_path = "src/assets/email_body.html"

    @staticmethod
    def generate_otp(length=6):
        otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        return otp

    def format_message(self, otp):
        with open(self.message_template_path, 'r') as html_file:
            html_file_content = html_file.read().replace("hschcsbbkk", str(otp))

        html_content = html_file_content
        html_part = MIMEText(html_content, "html")
        message = MIMEMultipart("alternative")
        message.attach(html_part)
        message["subject"] = "Verification"
        return message

    def send_otp(self, otp, recipient_email):
        sender_email = "snowwing14@gmail.com"
        password = "nsxw xpoo rnup cwzs"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, self.format_message(otp).as_string())

    def verify(self, recipient_email, key):
        placeholder = key / 10
        key = key % 10
        otp = self.generate_otp(5)
        self.send_otp(otp, recipient_email)

        print("Waiting for OTP...")
        time.sleep(5)
        entered_otp = input("Enter the OTP you received: ")

        modified_otp = otp[:placeholder]+key+otp[placeholder:]

        if entered_otp == modified_otp:
            print("Authentication successful!")
        else:
            print("Invalid OTP. Authentication failed.")

    def create(self):
        while True:
            placeholder = random.randint(0, 5)
            key = random.randint(0, 9)

            if placeholder != key:
                return placeholder * 10 + key
