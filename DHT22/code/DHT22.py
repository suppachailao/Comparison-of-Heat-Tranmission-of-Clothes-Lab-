import serial
import numpy
import pickle
import matplotlib.pyplot as plt 
from pathlib import Path
from drawnow import*

CtempC = [] #temp of our cloth
DtempC = []
arduinoData = serial.Serial('\\COM5', 115200, timeout=2) #create our serial object
plt.ion()
switch = True
show = -50


def makeFig():
	plt.ylim(22, 35) #set ymin and ymax value
	plt.title('My Live Streaming Data')
	plt.grid(True)
	plt.ylabel('Temp C')
	plt.xlabel('Time (6 second)')
	plt.plot(CtempC[show:], 'ro-', label='Cloth Temp C')
	plt.legend(loc='upper left')
	plt.plot(DtempC[show:], 'b^-', label='Envir Temp C')
	plt.legend(loc ='upper right')
	plt.show()

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

count = 0
exit_count = 50

while switch:

	while (arduinoData.inWaiting()==0): #Wait here until there is data
	    pass #do nothing

	read = arduinoData.readline()
	read = read.decode().strip('\r\n')
	dataArray = read.split(',')
	# print (dataArray[0])
	# print (dataArray[1])

	if len(dataArray[0]) > 0 and isfloat(dataArray[0]):
		CtempC.append(float(dataArray[0]))
		DtempC.append(float(dataArray[1]))

	else:
		CtempC.append(0.) #no detect

	drawnow(makeFig)
	plt.pause(.000001)
	count += 1

	if count >= exit_count:
		with open('CtempC_blackA_25W', 'wb') as fp:
			pickle.dump(CtempC, fp)
		with open('DtempC_blackA_25W', 'wb') as fp:
			pickle.dump(DtempC, fp)

		switch = False


print ()