# app/utils/email_utils.py

import smtplib


def send_email(
    recipient_email: str, subject: str, body: str, sender_email: str = None
) -> None:
    """Sends an email."""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your_email_address", "your_email_password")

    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email or "your_email_address", recipient_email, message)
    server.quit()

