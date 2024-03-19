#!/bin/bash

result=$(yad --entry --title '' --text '<span font="Firacode Nerd Font" font-size="x-large">Exit i3? (y/n):</span>' --text-align=center --no-buttons --skip-taskbar)

if [ "$result" == 'y' ] || [ "$result" == 'e' ]; then
    i3-msg exit
fi
