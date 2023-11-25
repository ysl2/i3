#!/bin/bash

if [ "$1" == '2' ]; then
    result=$(zenity --entry --text 'Choose a workspace to rename:')
else
    result=$(i3-msg -t get_workspaces | jq '.[] | select(.focused==true).name' | cut -d"\"" -f2)
fi
if [ -z "$result" ]; then
    exit 0
fi

result1=$(zenity --entry --text "Rename workspace ${result} to workspace:")
if [ -z "$result1" ]; then
    exit 0
fi

i3-msg rename workspace "$result" to 'temp'
i3-msg rename workspace "$result1" to "$result"
i3-msg rename workspace 'temp' to "$result1"
