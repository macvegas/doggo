#!/usr/bin/bash
if [[ $# = 0 ]]; then
	cat $DOGGO_PATH/manual.txt

fi
#allows the user to change the amount of saved paths in directories.txt
if [[ $1 = "-mem" ]]; then
	memory=$2
	matching='^[0-9][0-9]*$'
	if ! [[ $memory =~ $matching ]];then
		echo "doggo is confused, doggo only knows integers !"
	else
		sed -i "s/\(NumberOfSavedPaths=\)[0-9]*/\1$memory/" $DOGGO_PATH/only_one_line.py
		echo "doggo will now remember $memory paths."
	fi
fi