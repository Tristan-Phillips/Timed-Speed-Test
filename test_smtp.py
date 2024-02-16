import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'x'
SMTP_PORT = x
SMTP_USERNAME = 'x'
SMTP_PASSWORD = 'x'
FROM = 'x'
TO = 'x'

msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test Email'
msg['From'] = FROM
msg['To'] = TO

# Connect to the server and send the email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Use TLS
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.send_message(msg)
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print("Failed to send email:", e)