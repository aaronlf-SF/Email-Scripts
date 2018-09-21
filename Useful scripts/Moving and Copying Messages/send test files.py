
import os
import imaplib
import imaplib_connect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'my email'
email_password = 'password'
email_send = 'receiver email'

subject = "Test to move emails and delete attachments"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
msg.set_unixfrom(email_user)
print(msg.__dict__)
print(msg.get_unixfrom())

msg1 = msg
msg2 = msg

body = 'this is a test'
msg.attach(MIMEText(body,'plain'))
#print(msg.get_payload(decode=True)[0].as_string())

path = 'C:/Users/AFitzpatrick/Desktop/test_files/'
attachment_list = os.listdir(path)

for file_name in attachment_list:
	try:
		part = MIMEBase('application', "octet-stream")
		part.set_payload(open(path+file_name, "rb").read())
		
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
		msg.attach(part)
	except:
		print("could not attach file")

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
#SECURE LOGIN CALL WITH STARTTLS()
server.starttls()
server.login(email_user,email_password)

#server.sendmail(email_user,email_send,text)
server.quit()