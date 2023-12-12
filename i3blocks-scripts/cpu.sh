#!/bin/bash
echo "Cpu:$(top -bn1 | grep "%Cpu(s)" | awk '{print $2}' | cut -d "." -f 1)% "
