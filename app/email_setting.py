
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings


class EmailService:
    def __init__(self, user_email: str, subject: str, body: str):
        self.user_email = user_email
        self.subject = subject
        self.body = body

    def send_message(self):
        # Create odj. letter
        msg = MIMEMultipart()
        msg["From"] = settings.SMTP_USER_NAME
        msg["To"] = self.user_email
        msg["Subject"] = self.subject

        # Add text letter
        msg.attach(MIMEText(self.body, "plain"))

        # Connect to the SMTP server and send a letter
        try:

            server = smtplib.SMTP_SSL(settings.SMTP_SERVER, settings.SMTP_PORT)
            # server.starttls()
            server.login(settings.SMTP_USER_NAME, settings.SMTP_PASSWORD)
            server.sendmail(settings.SMTP_USER_NAME, self.user_email, msg.as_string())
            server.quit()

        except Exception as e:
            # Handling errors when sending
            print(f"Error send message: {str(e)}")
