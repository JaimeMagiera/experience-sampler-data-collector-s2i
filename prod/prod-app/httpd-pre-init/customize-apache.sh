#!/bin/bash
# This script is run before the Apache server starts. 

# Modify the cgi-bin folder path to accomodate the default application root of the image.
sed -i 's#/opt/rh/httpd24/root/var/www/cgi-bin#/opt/app-root/src/cgi-bin#g' /etc/httpd/conf/httpd.conf

# Set an httpd environment variable based on the container environment variable. This is the location where the data files with be written. 
if [[ -v DATA_DIR ]]; then
	echo "SetEnv DATA_DIR ${DATA_DIR}" >> /etc/httpd/conf/httpd.conf
fi
