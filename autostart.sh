#!/bin/sh

# ==============
# === Common ===
# ==============
# -> picom, natural scrolling, keyboard, etc.
[ -f ~/.vocal/0/scripts/wm/autostart_x11.sh ] && ~/.vocal/0/scripts/wm/autostart_x11.sh


# ===============
# === I3 spec ===
# ===============
# i3-autolayout autolayout &
autotiling &
# ~/.config/i3/scripts/i3/autostart/swallow.py &
~/.config/i3/scripts/i3/autostart/sticky_nofocus.py &
~/.config/i3/scripts/i3/autostart/nofullscreen.py &
# i3expod &


# ========================
# === Localhost config ===
# ========================
[ -f ~/.config/i3/autostart.localhost.sh ] && ~/.config/i3/autostart.localhost.sh
