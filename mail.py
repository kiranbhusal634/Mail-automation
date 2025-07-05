import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your Gmail credentials
sender_email = "nep*********@gmail.com"
sender_password = "***********"

# Recipient list
recipients = [
    '''add your recipients here'''
]

# Email content
subject = "Chess Tournament by NSU WRC 080"

body = """
Dear Participant,

Thanks for filling out the form for the Chess Tournament organized by NSU WRC 080 batch.

🕒 Time: 1:30 PM  
📍 Venue: BP Park  

Below is your Tie Sheet for Round 1. Further detailed tie sheets will be sent after the first round, as immediate registrations will also be considered tomorrow.

==============================
Chess Tournament Tiesheet - Round 1
==============================

Match 1:   
Match 2: 
Match 3:   
Match 4:   
Match 5:  
Match 6: 

We look forward to seeing you at the tournament!

Best Regards,  

"""

# SMTP setup
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server.send_message(msg)
        print(f"Email sent to {recipient}")

    server.quit()
    print("\nAll emails sent successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
