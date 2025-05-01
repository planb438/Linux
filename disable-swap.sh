#!/bin/bash 

# Disable swap and update /etc/fstab
# This script disables swap and comments out all swap entries in /etc/fstab
#     echo "Gzip command is not available."
# fi
#     echo "Gzip command is not available."
# fi
# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi
# Check if swap is enabled
if ! swapon --show | grep -q "swap"; then
    echo "Swap is already disabled."
    exit 0
fi
# Check if the system is using swap
if [ "$(free | grep Swap | awk '{print $2}')" -eq 0 ]; then
    echo "Swap is already disabled."
    exit 0
fi
# Check if the system is using swap
if [ "$(free | grep Swap | awk '{print $2}')" -eq 0 ]; then
    echo "Swap is already
