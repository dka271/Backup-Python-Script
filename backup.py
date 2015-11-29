#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os

path = os.getcwd()

sender = "dka271@vt.edu"
recipient = "dka271@vt.edu"

message = MIMEMultipart()

message[ 'From' ] = sender
message[ 'To' ] = recipient
message[ 'Subject' ] = "This is a back-up of a tar file"

textBody = "Body of the text"

message.attach(MIMEText(textBody, 'plain'))

fileName = "testTar.tar"
path = path + "/" + fileName
attachment = open(path, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % fileName)

message.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, "Medaridley-1")
text = message.as_string()
server.sendmail(sender, recipient, text)
server.quit()

