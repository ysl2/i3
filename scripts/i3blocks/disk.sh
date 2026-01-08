#!/bin/bash
echo "Disk:$(df -Ph / | awk 'NR==2{print $3 "/" $2}') "
