import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

#checkalert function for checking the alert for attack
def checkalert(i):
    print("Scanning For Malicious Traffic")
    while i != 0: 
          word_to_find='Detection of a Denial of Service Attack'
          with open("/var/log/snort/alert", "r+") as f:   

                if word_to_find in f.read():     
                   print("Alert! Danger")
                   time.sleep(60)
                   alertmail() #executing the alertemail function
                   print("Alert Email Sent to Administrator")
                   f.truncate(0)
                   break
                else:
                   pass#print("string not found")
    
          i = i + 1


#alertemail function for sending email
def alertmail():
   
    from_address = "lakshyanagpal16@gmail.com"
    to_address = "torque1906@gmail.com"
   

    message = MIMEMultipart() 
  
# storing the senders email address   
    message['From'] = from_address 
  
# storing the receivers email address  
    message['To'] = to_address
  
# storing the subject  
    message['Subject'] = "alert email"
  
# storing the body of the mail 
    body = "this is alert email"
  
# attaching the body
    message.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
    filename = "alert.txt"
    attachment = open("/var/log/snort/alert", "rb") 
  
# instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
    p.set_payload((attachment).read()) 
  
    encoders.encode_base64(p) 
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
   
    message.attach(p) 
  
# SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# starting the TLS for security 
    s.starttls() 
  
# login 
    s.login("lakshyanagpal16@gmail.com", "12324113a") 
    text = message.as_string()
    s.sendmail(from_address, to_address, text) 
    s.quit()


#main function
if __name__ == "__main__":
      i = 1
      j = 1
      while j != 0:
          checkalert(i)     # executing check alert function
      j = j + 1 
