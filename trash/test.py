import smtplib
server= smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
sender=input('Enter sender user mail id : ')
password=input('Enter password: ')
receiver = input("Enter receiver mail id")
server.login(sender,password)
server.sendmail(sender,receiver,'test','header')
server.quit()
