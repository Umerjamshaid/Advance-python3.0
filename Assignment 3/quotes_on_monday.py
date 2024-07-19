import smtplib
import pandas as pd
from datetime import datetime

# SMTP email server details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "umerjamshaid481@gmail.com"
GMAIL_PASSWORD = "vtut fiwi gaxh khve"


def send_email(to_address, subject, message):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(GMAIL_USER, to_address, email_message)
        print(f"Successfully sent email to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def is_monday():
    return datetime.today().weekday() == 0  # 0 represents Monday

def check_and_send_wishes():
    if not is_monday():
        print("Today is not Monday. Emails will not be sent.")
        return
    
    today = datetime.today()
    month = today.month
    day = today.day

    # Read the birthday CSV file
    birthdays = pd.read_csv('birthdays.csv')
    # birthdays = pd.read_csv('F:\BanoQabil Advanced.Py\Assignment 3\combined.txt', delimiter=",")

    for index, row in birthdays.iterrows():
        # if row["month"] == month and row["day"] == day:
            birthdays_today = birthdays[(birthdays["month"] == month) & (birthdays["day"] == day)]
            name = row["name"]
            email = row["email"]
            subject = "Happy Birthday!"
            message = (
            f"Dear {name},\n\n"
            f"On this special day, we celebrate you and all the joy you bring. "
            f"May your day be filled with laughter, love, and wonderful memories. "
            f"Wishing you a fantastic birthday and a year ahead filled with success and happiness.\n\n"
            f"Best Regards,\n"
            f"Your Friend"
        )
        send_email(email, subject, message)

        print("Emails sent successfully!")


if __name__ == "__main__":
    check_and_send_wishes()
