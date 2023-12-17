#!/bin/sh

# Common
~/.scripts/window-manager/autostart.sh # -> picom, natural scrolling, keyboard, etc.

# I3 spec.
autotiling &
~/.config/i3/i3-scripts/swallow.py &
~/.config/i3/i3-scripts/sticky_nofocus.py &

# Localhost config
[ -f ~/.config/i3/autostart.localhost.sh ] && ~/.config/i3/autostart.localhost.sh
