"""A python class library for creating something called a hash map that
	is capable of storing name value pairs in a data structure that is 
	efficient to retrieve values based on provided names.
	
	This rendition only allows a single value for each name.
	"""
	
# This first function is an initializer
def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets.  Default = 256 buckets"""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	
	#Results in aMap = [[], [], [], ... ]  (a list of empty lists)
	return aMap

def hash_key(aMap, key):
	"""Given a key, this will create a number and then convert it to an index for the aMap's buckets."""
	# hash the key then modulo the resulting int by the number of available buckets. 
	# this ensures very large numbers can still be distributed among a smaller
	# number of buckets.
	# len gets the number of items (buckets) in the provided hash map (aMap)
	return hash(key) % len(aMap)
	
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	# get the bucket id for a particular aMap object based on key
	bucket_id = hash_key(aMap, key)
	# return the list item (bucket) referenced by the bucket_id
	return aMap[bucket_id]
	
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and a value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)
	
	#for lists, enumerate returns each indices followed by the contents found at that index.
	#the bucket is a list of lists.  The lists contained are empty or contain tuples with a name value pair.
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			#found the key!
			return i, k, v
	
	# guess we didn't find the key after going through all in this bucket.
	return -1, key, default
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default)
	return v
	
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if i >= 0:
		# the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not, append to create it
		bucket.append((key, value))
		
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break
			
def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v

				

	