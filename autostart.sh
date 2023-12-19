#!/bin/sh

# ==============
# === Common ===
# ==============
# -> picom, natural scrolling, keyboard, etc.
[ -f ~/.scripts/window-manager/autostart.sh ] && ~/.scripts/window-manager/autostart.sh


# ===============
# === I3 spec ===
# ===============
i3-autolayout autolayout &
~/.config/i3/autostart/swallow.py &
~/.config/i3/autostart/sticky_nofocus.py &


# ========================
# === Localhost config ===
# ========================
[ -f ~/.config/i3/autostart.localhost.sh ] && ~/.config/i3/autostart.localhost.sh
