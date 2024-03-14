#!/bin/bash

result=$(zenity --entry --title '' --text 'Exit i3? (y/n):')

if [ "$result" == 'y' ] || [ "$result" == 'e' ]; then
    i3-msg exit
fi
