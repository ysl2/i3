#!/bin/bash
echo "Mem:$(free -h | awk '/^Mem/ {print $3 "/" $2}') "
