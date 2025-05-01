#!/bin/bash         
# Log Rotation Script
# This script rotates logs for a web server and compresses old logs

# Rotate logs
logrotate -f /etc/logrotate.conf
# Compress old logs
gzip /var/log/apache2/*.log
# Restart web server to apply changes
service apache2 restart
# Check if the service restarted successfully
if [ $? -eq 0 ]; then
    echo "Log rotation and compression completed successfully."
else
    echo "Failed to restart the web server."
fi
# Check if logrotate ran successfully
if [ $? -eq 0 ]; then
    echo "Log rotation completed successfully."
else
    echo "Log rotation failed."
fi
# Check if gzip ran successfully
if [ $? -eq 0 ]; then
    echo "Log compression completed successfully."
else
    echo "Log compression failed."
fi
# Check if the logrotate configuration file exists          
if [ -f /etc/logrotate.conf ]; then
    echo "Logrotate configuration file exists."
else
    echo "Logrotate configuration file does not exist."
fi
# Check if the log directory exists
if [ -d /var/log/apache2 ]; then
    echo "Log directory exists."
else
    echo "Log directory does not exist."
fi




# Check if the web server is running            
if pgrep apache2 > /dev/null; then
    echo "Web server is running."
else
    echo "Web server is not running."
fi
# Check if the logrotate command is available
if command -v logrotate > /dev/null; then
    echo "Logrotate command is available."
else
    echo "Logrotate command is not available."
fi
# Check if the gzip command is available
if command -v gzip > /dev/null; then
    echo "Gzip command is available."
else
    echo "Gzip command is not available."
fi
# Check if the service command is available
if command -v service > /dev/null; then
    echo "Service command is available."
else
    echo "Service command is not available."
fi
