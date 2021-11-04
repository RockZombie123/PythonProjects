#!/bin/bash

HEIGHT=15
WIDTH=40
CHOICE_HEIGHT=4
BACKTITLE="< Quit"
TITLE="Menu"
MENU="Choose one of the following categories:"

OPTIONS=(1 "Applications"
         2 "Root"
	 3 "Help"
	 4 "Credits"
         5 "Games")

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
	    chmod +x apps.sh
	    ./apps.sh
            ;;
        2)
            echo "You chose Option 2"
	    chmod +x root.sh
	    ./root.sh
            ;;


	3)
	   echo "You chose Option 3"
	   chmod +x help.sh
	   ./help.sh
	   ;;
	
	4)
	  echo "You chose Option 4"
	  chmod +x credits.sh
	  ./credits.sh
	  ;;
	
        5)
            echo "You chose Option 4"
	    chmod +x games.sh
	    ./games.sh
            ;;
esac
