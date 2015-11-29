#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os
import sys
import tarfile
import datetime

currentTime= str( datetime.datetime.now() )

path = os.getcwd()

if (len(sys.argv) != 2):
	print("You must enter a directory")
	exit()

sender = "dka271@vt.edu"
recipient = "dka271@vt.edu"

message = MIMEMultipart()

message[ 'From' ] = sender
message[ 'To' ] = recipient
message[ 'Subject' ] = "This is a back-up of "+ sys.argv[1] + " on " + currentTime

textBody = "Directory passed in: " +  sys.argv[1] + "\nTime it was backed up: " + currentTime
message.attach(MIMEText(textBody, 'plain'))

with tarfile.open("tarfile.tar.gz", mode='w:gz') as archive:
	archive.add(sys.argv[1], recursive=True)

fileName = "tarfile.tar.gz"
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

