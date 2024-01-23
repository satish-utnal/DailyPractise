import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Test'
msg['From'] = 'satisg.utnal@gmail.com'
msg['To'] = 'satisg.utnal@gmail.com'
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
