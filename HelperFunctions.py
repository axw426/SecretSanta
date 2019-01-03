import random
from copy import deepcopy

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

	
