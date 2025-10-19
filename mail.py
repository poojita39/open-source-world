import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is an automated message.")
msg["Subject"] = "Test Mail"
msg["From"] = "sender@example.com"
msg["To"] = "receiver@example.com"

with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.starttls()
    s.login("sender@example.com", "app_password")
    s.send_message(msg)
print("Mail sent.")
