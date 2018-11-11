#Created for open pickle 

import pickle 
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt


par = Path.cwd().parent
dataP = par / 'data'
# print (pa)

def plott(fName):

	#fName is a folder name
	nC, nD = 'CtempC_'+fName, 'DtempC_'+fName 
	fC = pa / fName / nC
	fD = pa / fName / nD
	print (fC.name, ' , ',fD.name)

	with open(fC, 'rb') as fp:
		CtempC = pickle.load(fp)

	with open(fD, 'rb') as fp:
		DtempC = pickle.load(fp)

	labelC = fName
	labelD = 'Room'
	nlc, mlc = len(CtempC), len(DtempC)
	plt.title("Time vs Temperature")
	plt.xlabel('Time [second]', fontsize=12)
	plt.ylabel('Temperature [C]', fontsize=12)
	plt.plot(np.arange(0, nlc)*30, CtempC, label=labelC)
	plt.plot(np.arange(0, mlc)*30, DtempC, label=labelD)
	plt.grid(); plt.legend()
	

plott('greenB')

plt.show()
