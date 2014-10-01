#!/usr/bin/env python 

import smtplib, time
from email.mime.text import MIMEText

to_list = ['email0@example.com', 'email1@example.com']
from_email = 'email@example.com'

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login('username', 'password')

for to in to_list:
    msg = MIMEText('dlsdskdakldkadasklkdajhw82q28dsjdkl') # Unique message text for easy filtering
    msg['Subject'] = 'EmailPing'
    msg['From'] = from_email
    msg['To'] = to
    print msg.as_string()
    s.sendmail(from_email, [to], msg.as_string())

s.quit()

