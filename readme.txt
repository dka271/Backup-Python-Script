Readme for Backup-Python-Script

Use:
Compile using the "python" compiler
Call the actual script "backup.py"
Pass in a directory (and path if necessary) that you would like to be backed up and sent to your email

Example call:
python backup.py DirectoryName

IMPORTANT:
Before running this code, 3 lines (all denoted with comments "#NEEDS TO BE CHANGED") need to be changed: lines 30, 31, 67.
The user must change lines 30 and 31 to their email address.
The user must also change line 67 to their email password.

It is possible using this script to send from one email address to an entirely different email address, and in this case, the password required is for the sending email address.
However, this is not recommended.
This script is meant to be used as a backup script and should send from the users email address, and arrive again at the users email address.
If this script is used to send from one email address to a different email address, it will take a substantially larger amount of time.
