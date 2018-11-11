import serial
import numpy
import pickle
from pathlib import Path

CtempC = [] #temp of our cloth
DtempC = []
arduinoData = serial.Serial('\\COM5', 115200, timeout=2) #create our serial object
switch = True



def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

count = 0
exit_count = 40
nameC = 'CtempC_blackA_25W'
nameD = 'DtempC_blackB_25W'

while switch:


	while (arduinoData.inWaiting()==0): #Wait here until there is data
	    pass #do nothing


	read = arduinoData.readline()
	read = read.decode().strip('\r\n')
	dataArray = read.split(',')


	if len(dataArray[0]) > 0 and isfloat(dataArray[0]):
		CtempC.append(float(dataArray[0]))
		DtempC.append(float(dataArray[1]))

	else:
		CtempC.append(0.) #no detect

	count += 1
	print (count, dataArray[0], dataArray[1])

	if count >= exit_count:
		with open(nameC, 'wb') as fp:
			pickle.dump(CtempC, fp)
		with open(nameD, 'wb') as fp:
			pickle.dump(DtempC, fp)

		switch = False