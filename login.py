#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: akul08

import mechanize # To log in the page
import shlex	 # To split a command
import subprocess # To run a command

#cmd will contain  ["ping","-c1","google.com"]     
cmd = shlex.split("ping -c1 google.com")

try:
	""" This will Run the command and store its output in output."""
	output = subprocess.check_output(cmd)
	# print output
except subprocess.CalledProcessError,e:
	''' If the command failed, Open the Login page and Login. '''   	
	# Will print the command failed with its exit status
	
	br = mechanize.Browser()
	br.open("http://172.16.22.1/24online/webpages/clientloginfilter.jsp?loginstatus=null&logoutstatus=true&message=You+have+successfully+logged+off&liverequesttime=null&livemessage=null&url=null&isAccessDenied=false&fromlogout=null&sessionTimeout=-1.0&ipaddress=172.16.22.200&clientLoginReq=true")
	br.select_form(nr=0)
	br["username"]="admin"
	br["password"]="1234"
	response=(br.submit())
	f=response.geturl()
	
	# print "Login Done"
	

