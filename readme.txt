Readme for Backup-Python-Script

This script takes in a a directory (and it's path if necessary) and creates a tar ball from the archive. Then it emails the email currently set up within the script the tar ball as an attachment, denoting the time that the script was run and noting this inside of the email. Thus essentially backing up work.



Use:
Compile using the "python" compiler
Call the actual script "backup.py"
Pass in a directory (and path if necessary) that you would like to be backed up and sent to your email

Example call:
python backup.py DirectoryName

IMPORTANT:
Before running this code, 2 things:

1. The user must go into any Gmail account settings being used and must allow "access for less secure apps." If this is not turned on, then Gmail will flag the emails as threats and will not allow them to be sent. Once your are logged into your Gmail account, you may use the link below to access this option:

https://www.google.com/settings/security/lesssecureapps

2. Also 3 lines (all denoted with comments "#NEEDS TO BE CHANGED") need to be changed: lines 30, 31, 67.
The user must change lines 30 and 31 to their email address.
The user must also change line 67 to their email password.

It is possible using this script to send from one email address to an entirely different email address, and in this case, the password required is for the sending email address, and the recipient must allow for less secure apps on their account.
However, this is not recommended.
This script is meant to be used as a backup script and should send from the users email address, and arrive again at the users email address.
If this script is used to send from one email address to a different email address, it will take a substantially larger amount of time. 
