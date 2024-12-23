import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Email server configuration
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SENDER_EMAIL = os.getenv("SENDER_EMAIL", SMTP_USER)


def send_email(to_email: str, subject: str, body: str):
    """
    Sends an email to the specified recipient.
    """
    try:
        # Create the email content
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(message)
            print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        raise e


def send_verification_email(to_email: str, token: str):
    """
    Sends a verification email with a token link.
    """
    verification_link = f"http://localhost:8000/verify/{token}"
    subject = "Verify Your Email Address"
    body = (
        f"Hi,\n\n"
        f"Thank you for registering on our platform. To activate your account, please verify your email address by clicking the link below:\n\n"
        f"{verification_link}\n\n"
        f"If you did not request this, please ignore this email.\n\n"
        f"Best regards,\n"
        f"The Team"
    )
    send_email(to_email, subject, body)
