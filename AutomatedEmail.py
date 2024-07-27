import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Disconnect from the server
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def job():
    sender_email = "swastikraghav216@gmail.com"
    sender_password = "your_password"
    recipient_email = "swasrag@example.com"
    subject = "Test Email"
    body = "This is a test email sent from a Python script!"
    
    send_email(sender_email, sender_password, recipient_email, subject, body)

# Schedule the job every day at 7:00 PM
schedule.every().day.at("7:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)