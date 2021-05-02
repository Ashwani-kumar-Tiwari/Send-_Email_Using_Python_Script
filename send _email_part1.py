# myaccount.google.com\lesssecureapps
# myaccount.google.com\lesssecureapps
# set password in envoirment variable

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "main@gmail.com"
toaddr = ['example1@gmail.com', 'example2@gmail.com', 'example3@gmail.com']
msg = MIMEMultipart()

name = ['Name1', 'Name2']
topic = ['topic 1', 'topic 2']

msg['From'] = fromaddr
msg['To'] = (', ').join(toaddr)
msg['Subject'] = " New Test Mail"
body = "Hi Team, \n\n \t This is the assigned topic of every one \n \t " + name[0] + ": " + topic[0] + "\n\t " + name[1] + ": " + topic[1] + "\n\n Thanks Regards"

msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
