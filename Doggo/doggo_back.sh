#!/usr/bin/bash

#restrictions of the number of directories shown
python $DOGGO_PATH/only_one_line.py
#execution of the displaying and user interaction
python $DOGGO_PATH/doggo_back.py
#gets the wanted path, or "." if fails
path=$(cat $DOGGO_PATH/path.txt 2>/dev/null || echo "."  )
/usr/bin/rm -f $DOGGO_PATH/path.txt 
#update the directory you left from, in the list
pwd >> $DOGGO_PATH/directories.txt
#moves to the wanted directory
cd $path
