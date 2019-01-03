import random
from copy import deepcopy
import xlrd 
import smtplib, ssl
from validate_email import validate_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def attemptOrdering(people):

	remainingPeople=deepcopy(people)
	finalgiver=[]
	finalreceiver=[]

	for giver in people:
		#lazy code using random rather than iterator...
		receiver=remainingPeople[random.randint(0, len(remainingPeople)-1)]
		finalgiver.append(giver)
		finalreceiver.append(receiver)
		remainingPeople.remove(receiver)
	
	return finalgiver, finalreceiver
	
def failedUniqueTest(finalgiver,finalreceiver):
	for giver,receiver in zip(finalgiver,finalreceiver) :
		if giver ==receiver : 
		#	print("Failed unique test")
			return True
	return False	
	
def printResults(finalgiver,finalreceiver):
	for giver,receiver in zip(finalgiver,finalreceiver) :
		print (giver+" got "+receiver)
		
def failedBanList(finalgiver,finalreceiver,banlist) :
	for giver,receiver in zip(finalgiver,finalreceiver) :
		banned=banlist[giver]
		if receiver in banned : return True
	return False	
	
def readFile():
	people=[]
	emails={}
	banlist={}
	
	wb = xlrd.open_workbook("InputData.xlsx")
	sheet = wb.sheet_by_index(0) 
	for row in range(1,sheet.nrows):
		people.append(sheet.row_values(row)[0])
		emails[sheet.row_values(row)[0]]=sheet.row_values(row)[1]
		banlist[sheet.row_values(row)[0]]=sheet.row_values(row)[2:]
	
	return people,emails,banlist
	
def validateEmail(people,emails):
	#only checks if the @xx.xx exists, can't check if full email address is valid these days
	for person in people:
		if validate_email(emails[person],check_mx=True) == False:
			print(emails[person]+" not valid!!! \n")
			exit()
	
def sendEmails(finalgiver,finalreceiver, emails):
	fromaddr = "alasdairwinterswonderland@gmail.com"
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "WintersWonderland2018")
	for giver,receiver in zip(finalgiver,finalreceiver):

		toaddr = emails[giver]
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Secret Santa"
		 
		body = "Hi "+giver+", \n\nYou are buying for "+receiver+"!\n\n Regards,\nSanta"
		msg.attach(MIMEText(body, 'plain'))
		
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		
	server.quit()

	
