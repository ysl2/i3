#!/bin/bash

result=$(zenity --entry --text 'Move current container to workspace:')

if [ -n "$result" ]; then
    i3-msg move container to workspace "$result"\; workspace "$result"
fi
