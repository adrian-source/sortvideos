import os
import shutil
import string
import subprocess
import smtplib

shownames=[
	"Parks and Recreation",
	"Castle",
	"Misfits",
	"The Big Bang Theory",
	"Top Gear",
	"White Collar",
	"The IT Crowd",
	"So You Think You Can Dance",
	"Community"]

downloadpath = "/pathToOriginal/"
destinationpath = "/pathToDestination/"

toaddr="xxxxxxxxxxxxxxxxxxxxxxxxx"
username="xxxxxxxxxxxxxxxxxxxxxxxx"
password="xxxxxxxxxx!"
message="xxxxxxxxxxx"


for name in shownames:
	if not os.path.exists(destinationpath+name):
		print destinationpath+name
		os.makedirs(destinationpath+name)

def flattendir():
	for f in os.listdir(downloadpath):
		if os.path.isdir(downloadpath+f):
			for ff in os.listdir(downloadpath+f):
				if (".avi" in ff.lower() or ".mp4" in ff.lower() or ".mk4" in ff.lower()) and not "sample." in ff.lower():
					os.rename(downloadpath+f+"/"+ff, downloadpath+ff)
			shutil.rmtree(downloadpath+f)
		
def sortvideos():

	for f in os.listdir(downloadpath):
		if os.path.isdir(downloadpath+f):
			continue
		else:
			for name in shownames:
				matchcount = len(string.split(name, " "))
				for word in string.split(name, " "):
					if word.lower() in f.lower():
						matchcount = matchcount - 1
				if matchcount == 0:
					os.rename(downloadpath+f, destinationpath+name+"/"+f)
					subprocess.Popen(['notify-send', message, f])
					server = smtplib.SMTP('smtp.gmail.com', 587)  
					server.ehlo()
					server.starttls()  
					server.ehlo()
					server.login(username,password)  
					headers = "\r\n".join(["from: " + username,
                       			"subject: "message",
                       			"to: "+toaddr+,
                       			"mime-version: 1.0",
                       			"content-type: text/html"])

					content = headers + "\r\n\r\n" + f
					server.sendmail(username, toaddr, content)
					

					


									

flattendir();
sortvideos();


