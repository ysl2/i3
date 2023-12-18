#!/bin/sh

# Common
# -> picom, natural scrolling, keyboard, etc.
[ -f ~/.scripts/window-manager/autostart.sh ] && ~/.scripts/window-manager/autostart.sh

# I3 spec.
autotiling &
~/.config/i3/i3-scripts/swallow.py &
~/.config/i3/i3-scripts/sticky_nofocus.py &

# Localhost config
[ -f ~/.config/i3/autostart.localhost.sh ] && ~/.config/i3/autostart.localhost.sh
