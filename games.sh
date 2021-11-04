#!/bin/bash

HEIGHT=15
WIDTH=40
CHOICE_HEIGHT=4
BACKTITLE="< Menu"
TITLE="Games"
MENU="Choose one of the following Games:"

OPTIONS=(1 "Snake"
         2 "Simon Says"
         3 "Other games")

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
	    chmod +x snake.sh
            ./snake.sh
            ;;
        2)
            echo "You chose Option 2"
	    chmod +x simon.sh
            ./simon.sh
            ;;
        3)
	    echo "You chose Option 3"
	    chmod +x othergames.sh
	    ./othergames.sh
	    ;;
esac
