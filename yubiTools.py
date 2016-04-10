"""
Module contains a single method, getNextYubi(), for retrieving a yubikey code from a local file
Created: 20160401 JDH - Basic functionality of opening file getting yubikey from top line and deleting that line from file.
Updates:
	201604061156 JDH - Cleaned up IO by openinig files using 'with' statement.  Added generic Exception handling.
	201604061501 JDH - Added this help() documentation to module
"""
import sys

def getNextYubi():
	"""
	Function to retrieve a yubikey code from a local file called YubikeyStash.txt (hard coded).
	
	Retuns a dictionary object containing 3 elements pertaining to outcome.
		["status"] - a numeric status where 0 represents failure, 1 represents success.
		["message"] - a friendly description of the outcome.
		["value"] - a yubikey string or None depending on success or failure of the operation.
		["count"] - a count of remaining Yubikeys
	"""

	yubi_file_name = 'YubikeyStash.txt'
	nextYubi = ""
	yubis_left = 0
	outcome = {}
	
	# Controlled execution and exception handling.
	try:
		# open file for reading:
		#   1) get the first line (next yubikey) and 
		#   2) get all remaining lines which will be the content to write back to the file in the next step
		with open(yubi_file_name, 'r') as fin:
			nextYubi = fin.readline()
			data = fin.read()
			yubis_left = len(data.strip().split('\n'))
			
		# open file for writing and write back the content minus the first line from above
		with open(yubi_file_name, 'w') as fout:
			fout.write(data)
			
		# test to make sure the yubikey we retrieved is longer than zero characters
		if len(nextYubi) > 0:
			# Success. Set outcome accordingly
			outcome["status"] = 1
			outcome["message"] = "Success"
			outcome["value"] = nextYubi.strip()
			outcome["count"] = yubis_left
			
		else:
			# Failure. Set outcome accordingly
			outcome["status"] = 0
			outcome["message"] = "Error: Yubikey could not be retrieved. Time to recharge file."
			outcome["value"] = None
			outcome["count"] = yubis_left
	
	# Catchall for exceptions
	except Exception as e:
		outcome["status"] = 0
		outcome["message"] = e.strerror
		outcome["value"] = None
		outcome["count"] = None
				
	return outcome

