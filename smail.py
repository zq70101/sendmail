#!/usr/bin/python
#coding:utf-8

import os  
import sys  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.application import MIMEApplication  

def send_():
	#mail
	_user = "user"  
	_pwd  = "pwd"  
	_to   = "to"

	msg = MIMEMultipart()  
	msg["Subject"] = "test"  
	msg["From"]    = _user  
	msg["To"]      = _to 

  
	str_all ="<h2>TEST</h2>"
	part = MIMEText(str_all,'html','utf_8')  
	msg.attach(part)
  
	#part = MIMEApplication(open(path+"xxx.tar.gz",'rb').read())  
	#part.add_header('Content-Disposition', 'attachment', filename="xxx.tar.gz")  
	#msg.attach(part)  
    
	s = smtplib.SMTP("10.10.10.10", timeout=30)  
	s.login(_user, _pwd)  
	s.sendmail(_user, _to, msg.as_string())  
	s.close()
	  
if __name__ == "__main__":
	send_()
