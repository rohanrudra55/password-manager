import random
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def format_msg(otp):
    # MESSAGE
    # html_content = f"""
    # <html>
    #     <body>
    #         <h3>This is the OTP for Password Manager.</h3>
    #         <p>Enter the code below:</p>
    #         <h1 style="background-color: #fff2cc;" >{otp}</h1>
    #     </body>
    # </html>
    # """
    with open("message.html", 'r') as html_file:
        html_file_content = html_file.read().replace("hschcsbbkk", str(otp))

    html_content = html_file_content
    html_part = MIMEText(html_content, "html")
    message = MIMEMultipart("alternative")
    message.attach(html_part)
    message["subject"] = "Verification"
    return message


def generate_otp(length=6):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp


def send_otp_via_email(otp, recipient_email):
    sender_email = "snowwing14@gmail.com"
    password = "nsxw xpoo rnup cwzs"
    message = format_msg(otp)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())


def verify(recipient_email):
    otp = generate_otp()
    send_otp_via_email(otp, recipient_email)

    print("Waiting for OTP...")
    time.sleep(5)
    entered_otp = input("Enter the OTP you received: ")

    if entered_otp == otp:
        print("Authentication successful!")
    else:
        print("Invalid OTP. Authentication failed.")


if __name__ == "__main__":
    verify("jasomati1211@gmail.com")
