#!/bin/bash

result=$(GTK_THEME="$(cat ~/.config/gtk-3.0/settings.ini | grep gtk-theme-name | cut -d= -f2)" zenity --entry --title '' --text 'Exit i3? (y/n):')

if [ "$result" == 'y' ] || [ "$result" == 'e' ]; then
    i3-msg exit
fi
