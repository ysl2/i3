#!/bin/sh

# ==============
# === Common ===
# ==============
# -> picom, natural scrolling, keyboard, etc.
[ -f ~/.scripts/wm/autostart.sh ] && ~/.scripts/wm/autostart.sh


# ===============
# === I3 spec ===
# ===============
# i3-autolayout autolayout &
autotiling &
# ~/.config/i3/scripts/i3/autostart/swallow.py &
~/.config/i3/scripts/i3/autostart/sticky_nofocus.py &
~/.config/i3/scripts/i3/autostart/nofullscreen.py &


# ========================
# === Localhost config ===
# ========================
[ -f ~/.config/i3/autostart.localhost.sh ] && ~/.config/i3/autostart.localhost.sh
