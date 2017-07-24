# Script checking if there's only one line in directories.txt
# if not, leaves the last one.
import os
from library_doggo import *
#reading all the available paths and stores them in a list
file=open(workingPath+"/directories.txt","r")
lineList=file.read().splitlines()
file.close()


# getting rid of "." actual directories (useless to go where we already are)
longueur=len(lineList)
i=0
while(i< longueur):
	if (lineList[i]=="."):
		longueur= longueur -1
		del lineList[i]
	i=i+1

# history's restriction to unique paths, getting rid of unecessary doubles
longueur=len(lineList)
differentpaths=[]
i=0
while (i>-longueur):
	
	pathetic=lineList[i]

	if (pathetic not in differentpaths):
		differentpaths.append(pathetic)
		i=i-1
	else:
		del lineList[i]
		longueur=longueur-1


# history rectriction to X paths
i=0
NumberOfSavedPaths=5
longueur=len(lineList)
surplus=longueur-NumberOfSavedPaths
if (surplus>0):
	while (i<surplus):
		del lineList[i]
		i=i+1
 


#updates the directories file (cleanup)
os.remove(workingPath+"/directories.txt")
file=open(workingPath+"/directories.txt","w")
for i in lineList:
	file.write(i)
	file.write("\n")
