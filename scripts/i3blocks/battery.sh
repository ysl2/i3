#!/bin/bash

get_battery() {
    status_file=/sys/class/power_supply/BAT0/status
    capacity_file=/sys/class/power_supply/BAT0/capacity
    if [ ! -e "$status_file" ] || [ ! -e "$capacity_file" ]; then
        echo ''
        return
    fi

    status=$(cat "$status_file")
    # if [ "$status" = "Charging" ]; then
    #     battery_icon="󰐼"
    # elif [ "$status" = "Discharging" ]; then
    #     battery_icon=""
    # else
    #     battery_icon=""
    # fi

    capacity=$(cat "$capacity_file")
    if [ -z "$capacity" ]; then
        echo ''
        return
    fi

    # printf -v capacity "%3s" "$capacity"
    #echo "$battery_icon $capacity%"
    echo "Bat:$capacity%($status) "
}

get_battery
