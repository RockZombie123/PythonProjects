#!/bin/bash

HEIGHT=15
WIDTH=40
CHOICE_HEIGHT=4
BACKTITLE="< Menu"
TITLE="Applications"
MENU="Choose one of the following applications:"

OPTIONS=(1 "Terminal"
         2 "Music Player"
	 3 "Update"
         4 "ASCII Video Player")

CHOICE=$(dialog --clear \
                --backtitle "$BACKTITLE" \
                --title "$TITLE" \
                --menu "$MENU" \
                $HEIGHT $WIDTH $CHOICE_HEIGHT \
                "${OPTIONS[@]}" \
                2>&1 >/dev/tty)

clear
case $CHOICE in
        1)
            echo "You chose Option 1"
	    cd PythonProjects/
            python3 simulator.py
            ;;
        2)
            echo "You chose Option 2"
	    python3 musicplayer.py
            ;;

	3)
	   echo "Downloading from: https://github.com/RockZombie123/PythonProjects.git"
	   git clone https://github.com/RockZombie123/PythonProjects.git
	   ;;

        4)
            echo "You chose Option 4"
	    python3 asciivideo.py
            ;;
esac
