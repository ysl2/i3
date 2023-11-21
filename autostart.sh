#!/bin/bash

# Common
~/.scripts/window-manager/autostart.sh # -> picom, natural scrolling, keyboard, etc.

# I3 spec.
autotiling &
~/.config/i3/i3-scripts/swallow.py &

# Localhost config
[ -f ~/.config/i3/autostart.localhost.sh ] && ~/.config/i3/autostart.localhost.sh
