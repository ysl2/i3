#!/bin/bash

if [ "$1" == '2' ]; then
    result=$(zenity --entry --text 'Choose a workspace to place:')
else
    result=$(i3-msg -t get_workspaces | jq '.[] | select(.focused==true).name' | cut -d"\"" -f2)
fi
if [ -z "$result" ]; then
    exit 0
fi

result1=$(zenity --entry --text "Place workspace ${result} to monitor ([l]eft/[r]ight/[d]own/[u]p):")

case "$result1" in
    l|left)
        result1='left'
        ;;
    r|right)
        result1='right'
        ;;
    d|down)
        result1='down'
        ;;
    u|up)
        result1='up'
        ;;
    *)
        exit 0
        ;;
esac

i3-msg workspace "$result"\; move workspace to output "$result1"
