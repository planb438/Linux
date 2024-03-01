#!/bin/bash

# Set variables
IP_ADDRESS="your_ip_address"
SUBNET_MASK="your_subnet_mask"
GATEWAY="your_gateway"

# Configure network interface
ifconfig eth0 $IP_ADDRESS netmask $SUBNET_MASK up
route add default gw $GATEWAY
