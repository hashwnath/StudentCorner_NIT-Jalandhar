import smtplib
import schedule
import main
import time
import os
i=1
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('rishabcandy@gmail.com', 'umarani19')
print("hujw")
def mail():
  # server.sendmail('rishabcandy@gmail.com', 's.hashwanth531@gmail.com','SPAM')
  os.system('python main.py')
schedule.every(10).seconds.do(mail)
while i>=1:
  schedule.run_pending()
  time.sleep(1)
