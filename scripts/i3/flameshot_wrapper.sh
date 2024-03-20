#!/bin/sh

export QT_QPA_PLATFORMTHEME=gtk3

if [ -z "$(pidof flameshot)" ]; then
    flameshot &
fi

focusedwindow_before=$(xdotool getactivewindow)

flameshot_option=$1
tesseract_option=$2

if [ -z "$tesseract_option" ]; then
    flameshot "$flameshot_option"
else
    TESSADTA_PREFIX=~/.vocal/tessdata_best \
    flameshot "$flameshot_option" --raw \
        | tesseract stdin stdout -l "$tesseract_option" \
        | xclip -in -selection clipboard
fi

[ -n "$focusedwindow_before" ] && [ "$focusedwindow_before" = "$(xdotool getactivewindow)" ] && xdotool windowfocus "$focusedwindow_before"
