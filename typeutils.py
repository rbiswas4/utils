#!/usr/bin/env python

import collections

def isiterable ( var ) :
	"""
	returns True if var is an iterable quantity, False otherwise
	
	args:
		var: mandatory, anytype
	returns : bool 
		True if iterable, False otherwise
	example_usage:
		if io.isiterable(k) :	
			k = np.asarray(k)
	status:
		tested, and works. 
		R. Biswas, Wed Oct  9 11:05:12 CDT 2013
	"""
	return isinstance(var , collections.Iterable)

