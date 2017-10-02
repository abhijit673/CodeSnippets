#! python3
#
# Script to send Text and HTML email
#

import pyautogui
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Standard mail configuration
# Password in Base64 encryption
encryptedPwd = b'SzBuZEBwdXI='
smtp_server = 'abc.xyz.com'
smtp_port = 465
username = 'John.Doe@xyz.com'
password = base64.b64decode(encryptedPwd).decode('ascii')

mailsubject = 'Details'
mailbody = 'Please fill in your details for this week \n\nRegards,\nJohn Doe'

# Set the email addresses 
fromaddr = 'from@xyz.com'
toaddr = 'receiver1@xyz.com;receiver2@xyz.com'
ccaddr = 'receiver3@xyz.com'
bccaddr = ''

# Set the parameters
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['cc'] = ccaddr
msg['bcc'] = bccaddr
msg['Subject'] = mailsubject
#msg.attach(MIMEText(mailbody, 'plain'))

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Connect to the mail server and send the mail
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
#server.starttls()
server.login(username, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
