#!/bin/sh

focusedwindow_before=$(xdotool getactivewindow)

if [ -z "$1" ]; then
    flameshot gui
else
    TESSADTA_PREFIX=~/.vocal/tessdata_best \
    flameshot gui --raw \
        | tesseract stdin stdout -l "$1" \
        | xclip -in -selection clipboard
fi

[ "$focusedwindow_before" = "$(xdotool getactivewindow)" ] && xdotool windowfocus "$focusedwindow_before"
