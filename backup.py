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

#Gets the current time
currentTime= str( datetime.datetime.now() )

#Get the current path
path = os.getcwd()

#Checks to make sure that there is an argument
if (len(sys.argv) != 2):
	print("You must enter a directory")
	exit()

#Checks to make sure that the directory exists
if not (os.path.isdir(path)):
	print(path + " does not exist")
	exit()

#Sets the sender and recipient of the email
sender = "<ENTER YOUR EMAIL ADDRESS HERE>"	#CHANGE THIS LOCATION
recipient = "<ENTER YOUR EMAIL ADDRESS HERE>"	#CHANGE THIS LOCATION

#Sets the subject and applies To and From to the email
message = MIMEMultipart()
message[ 'From' ] = sender
message[ 'To' ] = recipient
message[ 'Subject' ] = "This is a back-up of "+ sys.argv[1] + " on " + currentTime

#Sets and attaches the body text for the email
textBody = "Directory passed in: " +  sys.argv[1] + "\nTime it was backed up: " + currentTime
message.attach(MIMEText(textBody, 'plain'))

#Recursively creates the tar file
with tarfile.open("tarfile.tar.gz", mode='w:gz') as archive:
	archive.add(sys.argv[1], recursive=True)

#Creates the tar file as an attachment
fileName = "tarfile.tar.gz"
path = path + "/" + fileName
attachment = open(path, "rb")

#Convert the file into base 64 for sending
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % fileName)

#Attach the file
message.attach(part)

#Removes the temporary tar file from the directory
os.remove(path)

#Actually connects securely to the server, and sends the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, "<ENTER YOUR EMAIL PASSWORD HERE(FOR SENDER EMAIL)>")	#CHANGE THIS LOCATION
text = message.as_string()
server.sendmail(sender, recipient, text)
server.quit()
