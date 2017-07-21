#!/usr/bin/bash
# this script is updating the directory of the Doggo's file.
# this script MUST BE with the following scripts to make Doggo works :
#	doggo.py
#	doggo.sh
#	doggo_back.py
#	doggo_back.sh
#	only_one_line.py
#	library_doggo.py


echo "Setting up aliases..."
directory=$(pwd)

echo "Setting up working path..."

#builds the environment variable which allows Doggo to work
if [[ $(grep "DOGGO_PATH=" /etc/environment) != "" ]]; then
	sed -i "/DOGGO_PATH=/d" /etc/environment
fi

echo "DOGGO_PATH=\"$directory\"" >> /etc/environment
export DOGGO_PATH=$directory

echo "done."


# builds the aliases and delete the existing ones
if [[ $(grep "alias doggo=" /root/.bashrc) != "" ]]; then
	sed -i "/alias doggo=/d" /root/.bashrc
fi
if [[ $(grep "alias goto=" /root/.bashrc) != "" ]]; then
	sed -i "/alias goto=/d" /root/.bashrc
fi
if [[ $(grep "alias goback=" /root/.bashrc) != "" ]]; then
	sed -i "/alias goback=/d" /root/.bashrc
fi

sed -i "/# User specific aliases and functions/a alias doggo='. \$DOGGO_PATH/doggoptions.sh'" /root/.bashrc 
sed -i "/# User specific aliases and functions/a alias goto='. \$DOGGO_PATH/doggo.sh'" /root/.bashrc 
sed -i "/# User specific aliases and functions/a alias goback='. \$DOGGO_PATH/doggo_back.sh'" /root/.bashrc
# activates the aliases for the current session
alias doggo='. $DOGGO_PATH/doggoptions.sh'
alias goto='. $DOGGO_PATH/doggo.sh'
alias goback='. $DOGGO_PATH/doggo_back.sh'

