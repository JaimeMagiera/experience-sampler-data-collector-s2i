#!/bin/bash
# This script is run before the Apache server starts. 

# Modify the cgi-bin folder path to accomodate the default application root of the image.
sed -i 's#/opt/rh/httpd24/root/var/www/cgi-bin#/opt/app-root/src/cgi-bin#g' /etc/httpd/conf/httpd.conf

# Check for the DATA_DIR environment variable. If it exists, set an httpd environment variable with that value. This is the path where the data files with be written to. 
if [[ -v DATA_DIR ]]; then
	echo "SetEnv DATA_DIR ${DATA_DIR}" >> /etc/httpd/conf/httpd.conf
else
	echo "No DATA_DIR defined."
fi
