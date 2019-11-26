from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

import pandas as pd
import numpy as np
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import threadconfig

df = pd.read_csv("/home/amanda/FYP/testcsv/test.csv")
uniqueColList = []


@python_app
def dropUniqueColumns(startColIndex, endColIndex, dFrame, uniqueColList):
   
	import pandas as pd
	import numpy as np
	
	df = pd.DataFrame()
	df = dFrame.iloc[: , np.r_[startColIndex : endColIndex]]
	numOfRows = df.shape[0]

	for col in df.columns:
		if len(df[col].unique()) == numOfRows:
			#df.drop(col,inplace=True,axis=1)
			uniqueColList.append(col)

    
	return uniqueColList



maxThreads = threadconfig.maxThreads

numOfCols = df.shape[1]
print(numOfCols)

lasThreadCols = 0

results = []

#one col per thread
if numOfCols <= maxThreads:
	for i in range (numOfCols):
		uList1 = dropUniqueColumns(0, i+1, df, uniqueColList)
		results.append(uList1)
		#dfNew = pd.concat([dfNew, df1] , axis=1)
		

elif numOfCols > maxThreads:
	print("test2")
	if (numOfCols % maxThreads == 0):
		eachThreadCols = numOfCols / maxThreads 
		for i in range (maxThreads):
			dropUniqueColumns(i,(i+eachThreadCols),df,uniqueColList).result()
			#dfNew = pd.concat([dfNew, df1] , axis=1)
		
	else:
		print("test3")
		eachThreadCols = numOfCols // (maxThreads-1)
		lasThreadCols = numOfCols % (maxThreads-1)
		for i in range (0,(maxThreads-1)*eachThreadCols, eachThreadCols):
			print ("i", i)
			print("i+eachThreadCols", (i+eachThreadCols))
			dropUniqueColumns(i,(i+eachThreadCols),df,uniqueColList).result()
			#dfNew = pd.concat([dfNew, df1], axis=1)

		print("last thread", (eachThreadCols * (maxThreads-1)))
		dropUniqueColumns((eachThreadCols * (maxThreads-1)),numOfCols,df,uniqueColList).result()
	
		#dfNew = pd.concat([dfNew, df2] , axis=1)



# wait for all apps to complete
[r.result() for r in results]

#dropUniqueColumns(0,58,df,uniqueColList).result()
print(uniqueColList)
df.drop(uniqueColList,inplace=True,axis=1)

df.to_csv("/home/amanda/FYP/testcsv/dropUniqueColumnsOUTPUT.csv", index = False, header=True)

