# Script de "go to !" automatique
# Partie GOTO ==> Path.txt / solutions.txt 
from library_doggo import *
import sys,os
from subprocess import call
import readline

# extraction of the searched file
file=None
try:
	file=sys.argv[1] 
	if file is not "":
		print("\nlooking for files or directories...")
except IndexError:
	#workingpath defined in library
	call(["bash",workingPath+"/doggoptions.sh"])
if (file==""):
	call(["bash",workingPath+"/doggoptions.sh"])
option=None
optionValue=None

# try:
# 	option=sys.argv[2]
# 	optionValue=sys.argv[3]
# except IndexError:
# 	pass

#builds a list of parameters given to the script and adapts the things to do.
if file is not None and file is not "" :
	typage=False
	try:
		
		for i in range (2,len(sys.argv)):
			if(sys.argv[i]=="-lvl"):
				optionValue=sys.argv[i+1]
			if(sys.argv[i]=="-mem"):
				call(["bash","doggoptions.sh","-mem",str(sys.argv[i+1])])
			if(sys.argv[i]=="-t"):
				typage=True
		# longueur=len(listoption)
		# while i<longueur:
		# 	if
	except:
		pass

	linestack=search(file,option,optionValue)
	if (linestack==[]):
		print("Doggo couldn't find anything.\n")
	else:
		displayList(linestack,typage)
		#path's selection by the user
		userinput=askUser()
		if (userinput==""):
			path=linestack[0]
		else:
			path=linestack[userinput-1]
		writePath(path)