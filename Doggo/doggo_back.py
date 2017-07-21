# Script de "go to !" automatique
# Partie GOBACK
import os,sys
from library_doggo import *
import readline

#getting the directories we went through
file=open(workingPath+"/directories.txt","r")
pathlines = file.read().splitlines()
file.close()

displayList(pathlines,False)

#asks the wanted directory (Enter key leads to the 4th automatically, q allows quit)
userinput=raw_input("path ? ")
try:
	userinput=int(userinput)
except:
	if (userinput=="q"):
		sys.exit()
	elif (userinput==""):
		pass
	else:
		userinput=input("path? (int)  ")

if (userinput==""):
	zoulou=pathlines[-2]
else:
	zoulou=pathlines[userinput-1]

#writing the chosen path in path.txt for the bash script

writePath(zoulou)