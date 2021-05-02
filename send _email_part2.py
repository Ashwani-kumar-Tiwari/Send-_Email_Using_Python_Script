
#import os
import smtplib
import imghdr
from email.message import EmailMessage
#from string import Template

EMAIL_ADDRESS = 'your mail Address'
EMAIL_PASSWORD = 'Password'

#contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Email Subject'
msg['From'] = 'Your Name'
msg['To'] = 'Receiver mail address'

#msg.set_content('This is a plain text email')
topic = ['D', 'E', 'F']

#Email body

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <p>Hi Team</P>
        <p>&emsp; This is a plain text email</p>
        <ul>
          <li>NameA: """ + topic[0] + """</li>
          <li>NameB: """ + topic[1] + """</li>
          <li>NameC: """ + topic[2] + """</li>
        </ul>
        <p><b>&emsp; Rules -</b></p>
        <ol>
            <p>Rule 1 : Wash your Hand <br> Rule 2 : Use Mask <br> Rule 3 : Keep 2 meter distance in public places</p>
            <li>This is a list 1.</li>
            <li>This is a list 2.</li>
            <li>This is a list 3.</li>
        </ol>
        <p>&emsp; Thanks & Regards <br> &emsp; Your Friend</p>
    </body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
