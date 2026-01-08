#!/bin/bash
echo "Mem:$(LC_ALL=C free -h | awk '/^Mem/ {print $3 "/" $2}') "
