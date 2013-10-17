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
		>>> if io.isiterable(k) :	
		>>>	k = np.asarray(k)

	status:
		tested, and works. 
		R. Biswas, Wed Oct  9 11:05:12 CDT 2013
	"""
	return isinstance(var , collections.Iterable)

def hasanyattrs (object ,returnlist = False):

	"""
	Checks if the object has any attributes (rather than a particular 
	attribute as implemented in python 2.7.5 function hasattr ) 

	args: 
		object : name of object 

	returns: 
		tuple, ( Bool, listof attributes) 
	example usage:
		>>> import typeutils as tu 
		>>> print tu.hasanyattrs(o ,True)
		
	status: 
		Tested and found to work as expected, 
		R. Biswas, Sun Oct 13 17:01:45 CDT 2013
		
	"""

	hasanyattrs = False 
	lst = object.attrs.items()
	if len(lst) !=0:
		hasanyattrs = True 

	return (hasanyattrs , lst )
