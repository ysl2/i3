#!/bin/bash

volume_info=$(amixer -M get Master)

# NOTE: Need to be refractored in the future.
volume=$(echo "$volume_info" | sed -n 's/.*\[\([0-9]\+\)%\].*/\1/p' | head -1)
mute=$(echo "$volume_info" | sed -n 's/.*\[\([a-z]\+\)\].*/\1/p' | head -1)

if [[ $mute == "off" ]]; then
  result="MUTE"
else
  result="${volume}%"
fi

echo "󰕾 $result"
