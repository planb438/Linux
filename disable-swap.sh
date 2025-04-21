#!/bin/bash

echo "Disabling swap now..."
sudo swapoff -a

echo "Commenting out all swap entries in /etc/fstab..."
sudo cp /etc/fstab /etc/fstab.bak
sudo sed -i '/\bswap\b/ s/^/#/' /etc/fstab

echo "✅ Swap disabled and /etc/fstab updated."
