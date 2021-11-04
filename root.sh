#!/bin/bash

HEIGHT=15
WIDTH=40
CHOICE_HEIGHT=4
BACKTITLE="< Applications"
TITLE="Root"
MENU="Choose one of the following files:"

OPTIONS=(1 "/home/s29sshankar/validation2.py"
         2 "/home/s29sshankar/PythonProjects/simulator.py"
         3 "/home/s29sshankar/menu.sh"
	 4 "/home/s29sshankar/root.sh"
	 5 "/home/s29sshankar/apps.sh")


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
            nano validation2.py
            ;;
        2)
            echo "You chose Option 2"
            cd PythonProjects
	    nano simulator.py
            ;;
        3)
            echo "You chose Option 3"
	    chmod +x menu.sh
	    nano menu.sh
	    ;;
	4)
            echo "You chose Option 4"
            chmod +x root.sh
            nano root.sh
            ;;
        5)
            echo "You chose Option 5"
            chmod +x apps.sh
            nano apps.sh
            ;;
esac          
