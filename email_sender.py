import smtplib
from email.message import EmailMessage

def send_email(receiver_email, file_path):

    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"  # 🔥 Use Gmail App Password

    msg = EmailMessage()
    msg['Subject'] = "Meeting Report"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content("Your meeting report is attached.")

    with open(file_path, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="meeting_report.pdf"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
