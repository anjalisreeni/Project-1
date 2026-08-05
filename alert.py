import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Assuming you are using python-dotenv to load environment variables
# from dotenv import load_dotenv
# load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_email_alert(subject: str, message: str) -> None:
    """
    Sends an email alert using SMTP configuration from environment variables.
    """
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    recipient_email = os.getenv("ALERT_RECIPIENT")

    if not all([sender_email, sender_password, recipient_email]):
        logger.error("Email credentials are not fully configured in the environment.")
        return

    # Create the email payload
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"[AtmoSync Alert] {subject}"

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Establish a secure session with the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # Login and send
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        
        logger.info(f"Alert email sent successfully to {recipient_email}")
    except Exception as e:
        logger.error(f"Failed to send email alert: {e}")
    finally:
        server.quit()

# Quick test execution
if __name__ == "__main__":
    send_email_alert(
        subject="High Temperature Detected", 
        message="Container 404 has exceeded the maximum temperature threshold."
    )