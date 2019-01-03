from copy import deepcopy
import HelperFunctions as hf

sendemails=True

people, emails, banlist=hf.readFile()
hf.validateEmail(people,emails)
	
i=0

while True:
	if i%100 ==99 :
		print("Really struggled to find a suitable combo after "+str(i+1)+" attempts.... is there even a possible combo?")
	if i==1000 :
		print("Gave up after "+str(i)+" attempts..")
		break		
	finalgiver,finalreceiver=hf.attemptOrdering(deepcopy(people))
	#check if it found a suitable combo, i.e. that it didn't run out of receivers
	if hf.failedUniqueTest(finalgiver,finalreceiver) == True: continue
	if hf.failedBanList(finalgiver,finalreceiver,banlist) ==True: continue
	hf.printResults(finalgiver,finalreceiver)
	if sendemails == True: hf.sendEmails(finalgiver,finalreceiver,emails)
	break	
