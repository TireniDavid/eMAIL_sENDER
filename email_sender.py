import os
from email.message import EmailMessage
import ssl, smtplib

email_sender = 'eldenbe17@gmail.com'
email_password = os.environ.get('EMAILPASSWORD')

email_receiver = 'tirenioluwa.adek@bulldogs.aamu.edu'

subject = "STOP MISSING OUT- take this chance"
html_body = '''
<html>
  <body> 
  <p> When you watch a video, please hit subscribe </p>
  <p>We appreciate your loyalty as we continue to bring you exciting content and deals.</p>
  <p>If you have any questions or feedback, feel free to reach out to us at <a href="mailto:eldenbe17@gmail.com">eldenbe17@gmail.com</a>.</p>
  <p>Stay tuned for more updates and exclusive offers!</p>
  <img src="cid:image1" alt = "Amazon image gift card">
  <br>It's more than just entertainment. It's an opportunity to become part of our community and support<br> the content you love.
  By hitting "subscribe," you not only stay updated with our latest releases but<br> also help us grow and create even more engaging 
  content for you. We value your support, and we're<br> committed to delivering the best content and deals to our subscribers. 
  Your loyalty inspires us to continue<br> our creative journey and bring you exciting content.If you ever have questions, feedback,
  or suggestions,<br> please don't hesitate to reach out to us. <br>
  
  <p>We'd love to hear from you. Thank you for being part of our community, and stay tuned for more updates, exclusive offers, and much more!</p>
  
  </body>
</html>
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(html_body, subtype= 'html')

#Attach an image inline

with open('AMAZON.png', 'rb') as img_file:
    img_data = img_file.read()
    em.add_attachment(img_data, maintype='image', subtype='png', cid='image1')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

