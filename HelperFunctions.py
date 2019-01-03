import random
from copy import deepcopy
import xlrd 

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

	
