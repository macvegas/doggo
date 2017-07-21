import sys,os
from subprocess import call
import readline
#nom d'un petard !
# function searching for a file and throwing back a list of possible paths
workingPath=os.environ.get('DOGGO_PATH')
# displayType= False
def search(file,option=None,optionValue=None):

	sortie=""

	#looks for matching files/directories and stores in solutions.txt
	# if (option=="-mem"):
	# 	call(["bash","doggoptions.sh",str(option),str(optionValue)])
	# 	option=None
	#check if there is an option, if not, basic goto
	if (option == None):

		sortie=os.popen("find / -iname \""+file+"\"", "r").read()

	#if option is -lvl, check if its value is a integer, if it is not, acts like doggo didn't find anything
	elif (option == "-lvl"):
		try:
			optionValue=int(optionValue)
		except:
			return([])
		# lookup the level asked by the user and does as many /.. as needed
		source="."
		for k in range(0,optionValue):
			source=source+"/.."
		sortie=os.popen("find $(cd "+source+"; pwd) -iname \""+file+"\"", "r").read()
# "find $(cd "+source+"; pwd) -iname \""+file+"\""

	file=open(workingPath+"/solutions.txt","w")
	file.write(sortie)
	file.close

	#extract each posible path into a list linestack
	file=open(workingPath+"/solutions.txt","r")
	linestack= file.read().splitlines()
	file.close
	os.remove(workingPath+"/solutions.txt")
	return(linestack)

def displayList(listing,typa):
	longueur=len(listing)
	for i in range(longueur):
		#displays the type of the file or not
		if typa==True:
			type=""
			#gets the only interresting part of the type command return
			chainetype=os.popen("file -b "+listing[i]).read()
			#simplify some types to make them short
			if (chainetype.split(",")[0]=="Bourne-Again shell script"):
				type="SHELL script"
			elif (chainetype.split(",")[0]=="ELF 64-bit LSB executable"):
				type="64 EXEcutable"
			elif (chainetype.split(",")[0]=="ELF 32-bit LSB executable"):
				type="32 EXEcutable"
			elif ("broken symbolic link to" in chainetype.split(",")[0] ):
				type="broken s.LINK"
			elif ("symbolic link to" in chainetype.split(",")[0] ):
				type="active s.LINK"
			elif ("cannot open (No such file or directory)" in chainetype.split(",")[0]):
				type="!-!-UNKNOWN-!-!"
			else:
				type=chainetype.split(",")[0]
			retour= (str(i+1)+" : ").ljust(6)+"|| "+('{:<10}'.format(type.strip())).center(18) +" || "+ listing[i]
			print retour
		else:
			print ((str(i+1)+" : ").ljust(6)+"|| " + listing[i])

def askUser():
	ui=raw_input("path ? ")
	try:
		ui=int(ui)
	except:
		if (ui=="q"):
			sys.exit()
		elif (ui==""):
			pass
		else:
			ui=input("integer needed. Path ? ")
	return ui

def writePath(path):
	if (os.path.isdir(path)):
		fichier = open(workingPath+"/path.txt","w")
		fichier.write(path)
		fichier.close
	else:
		path=os.path.dirname(path)
		fichier = open(workingPath+"/path.txt","w")
		fichier.write(path)
		fichier.close

def flag(inte):
	print("flag reached :"+ str(inte))