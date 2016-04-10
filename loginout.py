"""
 A set of tools for logging into various systems including those that require
 auth tokens such as YubiKeys.
 
Author: 
Jesse D. Hagberg

Created: 
2016-04-01 JDH - Created basic functions and format to solve 
				 compulsory logins for Daxtra employees
Updates: 
2016-04-06 JDH - Combined shared workflow of daxtra_login and 
     		     daxtra_logout into a worker function called daxtra_log
2016-04-07 JDH - Enhanced feedback from daxtra_log method indicating 
				 success/failure, friendly status message and number of 
				 yubikeys remaining	.
2016-04-08 JDH - Added this inline documentation
"""
from yubiTools import getNextYubi
import requests
from selenium import webdriver
import time
import bs4
import re
from sys import exit

def daxtra_login():
	"""
	Wrapper function for performing a daxtra employee login.
	"""
	return daxtra_log("in")

	
def daxtra_logout():
	"""
	Wrapper function for performing a daxtra employee logout.
	"""
	return daxtra_log("out")
	
	
def daxtra_log(inout):
	"""
	Function for performing a daxtra login or logout using an employee specific yubikey.
	"""
	outcome = {}
	url = 'http://in.daxtra.com/doaction.pl'
	
	# Attempt to get a Yubikey
	yubiResponse = getNextYubi()
	
	# Check we got a yubiKey and abort with message if not.
	if yubiResponse["status"]:
		outcome["yubiKeys_remaining"] = yubiResponse["count"]
	else:
		outcome["status"] = 0
		outcome["message"] = "Yubi Error: %s" % yubiResponse["message"]
		return outcome
		
	# Build the POST request
	form_data = {
		'user_yubi': '%s' % yubiResponse["value"],
		'action': 'sign' + inout + '',
		'location': 'home',
		'resource': 'Web+SignIn+Form HTTP/1.1'
	}
	
	# Make the request
	response = requests.post(url, data=form_data)

	# Check for a success message.  
	# r preceding the """ indicates a raw string
	# re.DOTALL is a compilation flag that makes the . match any character including newlines
	# re.VERBOSE causes the re.compile to ignore whitespace not found in a character class unless found after an unescaped backslash '\'
	# re.DOTALL and re.VERBOSE are logically OR'd  with '|' and passed to re.compile as a single combined compilation flag.
	pattern = re.compile(r"""
                          <h3>System\ Message: # Start of match string
                          .+?                  # Match one or more of any character (.+) but don't be greedy (?)
                          </p>                 # End of match string
                          """, re.VERBOSE | re.DOTALL)

	result = re.search(pattern, response.content)
	
	# Check the result and build the outcome message that is returned by this function
	# First check to see if the result (match object) actually exists.
	if result == None:
		outcome["status"] = 0
		outcome["message"] = "Error: \"System Message\" not found in response.  You're probably NOT logged %s." % inout
	# Next, test for Success.  Celebrate the wins!
	elif "Success" in result.group():
		outcome["status"] = 1
		outcome["message"] = "Success!  You are logged %s." % inout
	# Test for an explicit error
	elif "Error" in result.group():
		outcome["status"] = 0
		outcome["message"] = "Error: The page returned an error.  You're probably NOT logged %s." % inout
	# Handle the unexpected result.
	else:
		outcome["status"] = 0
		outcome["message"] = "Warning:  A response was returned but we did not detect either \"Success\" or \"Error\"."
			
	# Write the output to a file in case we need to inspect it later.  
	# The 'with' statement ensures the file stream is cleaned up/closed even if an exception occurs.	
	with open('daxtra_login_output.txt', 'w') as outputfile:
		outputfile.write(response.content)

	return outcome
	
	
def oiilogin(browser):
	"""
	TODO - create a function that will login to Out Island Internet's portal
		   using username and password stored in a file.
	"""
	pass
	

def oiikeepalive(snooze=60):
	"""
	WIP  - A method to maintain an active connection to Out Island Internet's
		   wireless portal.  A pre-requisite is actually being connected to 
		   an OII wireless access point. (no security but has login before use)
	"""

	# While True (escape with ctrl-C)
	count = 0
	
	# open a firefox browser to do our bidding
	browser = webdriver.Firefox()
	try:
		while True:
		
			count += 1
			
			# attempt to open google.bs
			print "Round %d, fight! (Attempting to access google.bs website.)" % count
			bowser.get("https://www.google.bs")
			
			# if title is <title>Google</title> then we're good.
			if True:
				
				# go to sleep for 10 minutes
				print "Still logged in!  Going sleep for %d minutes, boss." % snooze
			
			else:
			# if title is <title>Home - Out Island Internet</title then we're not logged in.
			
				print "Looks like those bastards timed us out."
				# login
				oiilogin()
				
			# go to sleep for x mintues
			time.sleep(snooze)
	except KeyboardInterrupt:
		print "Interrupted"
		browser.close()
		sys.exit(0)
