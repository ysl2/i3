#!/bin/bash

# ref: https://stackoverflow.com/questions/9229333/how-to-get-overall-cpu-usage-e-g-57-on-linux
# cpu=$(awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else printf "%.1f", ($2+$4-u1) * 100 / (t-t1) "%"; }' <(grep 'cpu ' /proc/stat) <(sleep .1;grep 'cpu ' /proc/stat))
# echo "Cpu:${cpu}% "

cpu=$(
    (
        grep '^cpu ' /proc/stat
        sleep 0.5
        grep '^cpu ' /proc/stat
    ) | awk '
    {
        total = 0
        for(i=2; i<=NF; i++) total += $i
    }
    NR==1 {
        total_prev = total
        idle_prev = $5
    }
    NR==2 {
        total_diff = total - total_prev
        idle_diff = $5 - idle_prev

        if (total_diff == 0) total_diff = 1

        cpu = (1 - (idle_diff / total_diff)) * 100
        printf "%.1f", cpu
    }
    '
)
echo "Cpu:${cpu}% "
