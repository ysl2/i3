#!/bin/bash
echo "Disk:$(df -h / | awk 'END{print $3 "/" $2}') "
