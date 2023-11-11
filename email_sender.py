import os
from email.message import EmailMessage
import ssl, smtplib

email_sender = 'eldenbe17@gmail.com'
email_password = os.environ.get('EMAILPASSWORD')
print("Retrieved Password:", email_password)



