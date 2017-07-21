#!/usr/bin/bash

#launches the search of wanted file
python $DOGGO_PATH/doggo.py "$1" $2 $3 $4 $5 $6
#creates, if not existing, a file where to write all the directories
touch $DOGGO_PATH/directories.txt
#extracts the chosen path and changes the current directory for it
line=$(cat $DOGGO_PATH/path.txt 2>/dev/null || echo "."  ) 
rm -f $DOGGO_PATH/path.txt 
cd $line 
#writes the path to the txt file
echo $line >> $DOGGO_PATH/directories.txt #&> /dev/null
#maintain the limit of written directories
python $DOGGO_PATH/only_one_line.py
