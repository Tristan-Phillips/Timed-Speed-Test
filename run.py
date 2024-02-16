import csv
import smtplib
import speedtest
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = 'x'
SMTP_PORT = x
SMTP_USERNAME = 'x'
SMPT_PASSWORD = 'x'

ISP_EMAIL = 'x'

def test_speed():
    try:
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
    except speedtest.ConfigRetrievalError as e:
        print(f"Failed to retrieve speedtest.net configuration: {e}")
        return
    except Exception as e:
        print(f"Failed to perform speed test: {e}")
        return

    data = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'download': s.download() / 8 / 1000000,  # Convert to MB/s
        'upload': s.upload() / 8 / 1000000,  # Convert to MB/s
        'ping': s.results.ping,
    }

    print(data)  # Print the results to the console

    try:
        with open('internet_speed_log.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writerow(data)
    except Exception as e:
        print(f"Failed to write to CSV file: {e}")

def send_email():
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your-username'
    PASSWORD = 'your-password'
    FROM = 'your-email@example.com'
    TO = 'recipient-email@example.com'

    # Create the message
    msg = MIMEText('This is a test email.')
    msg['Subject'] = 'Test Email'
    msg['From'] = FROM
    msg['To'] = TO

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=60)
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Schedule the  test to run every x
schedule.every(1).minutes.do(test_speed)

# Schedule the email to be sent every x minutes
schedule.every(3).minutes.do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)

