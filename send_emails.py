import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# ~~~ ENSURE GMAIL ALLOWS IMAP AND LESS SECURE APPS TO RUN BEFORE USING THIS SCRIPT ~~~ #

email_user = 'your email goes here'
email_password = 'your password goes here'
email_send = 'recipient email goes here'

subject = 'subject line goes here'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

#ADDING TEXT TO THE EMAIL
body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

#ADD AN ATTACHMENT TO THE EMAIL
directory = 'c:/users/blah blah/'
filename = 'filename.jpg'
attachment = open(directory + filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)

#LOGGING IN 
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

#SENDING THE EMAIL MESSAGE
server.sendmail(email_user,email_send,text)
server.quit()

#PRINTING THE EMAIL MESSAGE
text = msg.as_string()
print(text)
