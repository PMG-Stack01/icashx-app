import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from fastapi import HTTPException

# Optional: SendGrid client (recommended for Render)
try:
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
    SENDGRID_AVAILABLE = True
except ImportError:
    SENDGRID_AVAILABLE = False


# ==================================================
# Option 1️⃣ — Send via SendGrid API (preferred)
# ==================================================
def send_via_sendgrid(to_email: str, subject: str, message: str, attachment_path: str | None = None):
    """
    Sends an email using the SendGrid API.
    Required environment variable: SENDGRID_API_KEY
    """
    sendgrid_key = os.getenv("SENDGRID_API_KEY")
    if not sendgrid_key:
        raise HTTPException(status_code=500, detail="SendGrid API key not set in environment.")

    email = Mail(
        from_email=os.getenv("EMAIL_FROM", "no-reply@icashx.app"),
        to_emails=to_email,
        subject=subject,
        html_content=message
    )

    # Attach a file if provided (PDF, DOCX, etc.)
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            data = f.read()
        encoded_file = FileContent(data)
        attachedFile = Attachment(
            FileContent(encoded_file),
            FileName(os.path.basename(attachment_path)),
            FileType("application/octet-stream"),
            Disposition("attachment")
        )
        email.attachment = attachedFile

    sg = SendGridAPIClient(sendgrid_key)
    response = sg.send(email)
    return {"status": "sent", "to": to_email, "response_code": response.status_code}


# ==================================================
# Option 2️⃣ — Send via SMTP (fallback)
# ==================================================
def send_via_smtp(to_email: str, subject: str, message: str, attachment_path: str | None = None):
    """
    Sends an email using standard SMTP (like Gmail or Outlook).
    Required environment variables:
        EMAIL_HOST, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD
    """
    EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
    EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_FROM = os.getenv("EMAIL_FROM", EMAIL_USERNAME)

    if not (EMAIL_USERNAME and EMAIL_PASSWORD):
        raise HTTPException(status_code=500, detail="SMTP credentials are not configured.")

    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "html"))

    # Attachment handling
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header("Content-Disposition", "attachment", filename=os.path.basename(attachment_path))
            msg.attach(attach)

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.send_message(msg)

    return {"status": "sent", "to": to_email, "provider": "SMTP"}


# ==================================================
# Unified Helper
# ==================================================
def send_email(to_email: str, subject: str, body: str, attachment_path: str | None = None):
    """
    Chooses the best available method (SendGrid if present, else SMTP)
    """
    if SENDGRID_AVAILABLE and os.getenv("SENDGRID_API_KEY"):
        return send_via_sendgrid(to_email, subject, body, attachment_path)
    return send_via_smtp(to_email, subject, body, attachment_path)