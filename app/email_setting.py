import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from app.core.config import settings


def send_welcom_letter(user_email: str, donat_url: str):
    # Create text letter
    subject = "State Enterprise R&D Center for Overuse Issues of Georesources"
    body = f"Hello, thank you for your question. We will contact you shortly\n" \
           f" If we support Socrat project, follow the link for support {donat_url}"

    # Create odj. letter
    msg = MIMEMultipart()
    msg["From"] = settings.SMTP_USER_NAME
    msg["To"] = user_email
    msg["Subject"] = subject

    # Add text letter
    msg.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send a letter
    try:
        server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
        server.starttls()
        server.login(settings.SMTP_USER_NAME, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_USER_NAME, user_email, msg.as_string())
        server.quit()

    except Exception as e:
        # Handling errors when sending
        print(f"Error send message: {str(e)}")
