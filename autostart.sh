#!/bin/bash

# Common
~/.wm/autostart.sh # -> picom, natural scrolling, keyboard, etc.

# I3 spec.
autotiling &

# Localhost config
[ -f ~/.config/i3/autostart.localhost.sh ] && ~/.config/i3/autostart.localhost.sh
