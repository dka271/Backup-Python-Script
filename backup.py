#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

sender = "dka271@vt.edu"
recipient = "dka271@vt.edu"
message = MIMEMultipart()
message[ 'From' ] = sender
message[ 'To' ] = recipient
message[ 'Subject' ] = "Backup python script test"

textBody = "This is testing the text body"
message.attach(MIMEText(textBody, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, "Medaridley-1")
text = message.as_string()

server.sendmail(sender, recipient, text)
server.quit()
