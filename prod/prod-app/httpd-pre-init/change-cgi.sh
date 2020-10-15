#!/bin/bash
sed -i 's#/opt/rh/httpd24/root/var/www/cgi-bin#/opt/app-root/src/cgi-bin#g' /etc/httpd/conf/httpd.conf 
