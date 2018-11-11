
import pickle 
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt


par = Path.cwd().parent #parent 
dataP = par / 'data' #data folder
iterD = [leaf for leaf in dataP.iterdir()]

for i in range(0, len(iterD), 2):
	
	with open(iterD[i], 'rb') as cp:
		A = pickle.load(cp)
		print (iterD[i].name)

	with open(iterD[i+1], 'rb') as ep:
		B = pickle.load(ep)
		print (iterD[i+1].name, '\n')

	nA, nB = len(A), len(B)
	plt.plot(np.arange(0, nA)*30, A, label=iterD[i].name)
	plt.plot(np.arange(0, nB)*30, B, label=iterD[i+1].name)

plt.title("Time vs Temperature")
plt.xlabel('Time [second]', fontsize=12)
plt.ylabel('Temperature [C]', fontsize=12)
plt.grid(); plt.legend()
plt.show()






