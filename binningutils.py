#!/usr/bin/env python




import numpy as np
import math as pm
verbose = False


def nbinarray(numpyarray , 
		binningcol , 
		binsize , 
		binmin  , 
		binmax  ):
	"""
	bins a numpy array in equal bins in the variable in the column 
	of the array indexed by the integer binningcol. 

	args:
		binningcol: integer, mandatory
			integer indexing the column of the array holding the 
			variable wrt which we are binning
		binsize : float, mandatory

		binmins : float,  mandatory
		binmax  : float, mandatory
	returns: a numpy array of elements x corresponding to the bins. Each 
		element x is an array of the elements of in input numpyarray 
		that are assigned to the bin 

	example usage:

	notes:

	"""

	#First define the bins:
	numrows , numcols   = np.shape(numpyarray)
	numbins = int(pm.floor((binmax - binmin )/binsize))
	binningcolbins = np.linspace(binmin , binmax ,numbins+1)
	
	digitizedindex = np.digitize(numpyarray[:,binningcol],
			bins = binningcolbins)
	binnedarray = []
	for i in range(numbins):	
		binnedarray.append(numpyarray[digitizedindex==i+1])

	ret=  np.array(binnedarray)
	if verbose :
		print "size of bins" , map(len, ret)
	return ret

def ngetbinnedvec( nbinnedarray , col):
	"""Given an array of 2d numpy arrays (ie. having 
	shape (numrows, numcols), returns an array of 1d 
	numpy arrays composed of the col th column of the 
	2d arrays. 

	example useage :

	"""

	numbins = len(nbinnedarray)
	
	binnedvec = []
	for i in range(numbins):
		binnedvec.append(nbinnedarray[i][:,col])

	return binnedvec

if __name__ == "__main__":

	import sys
	import numpy as np
	import matplotlib.pyplot as plt

	num = 10 
		
		#basic model: x is independent variable, y, z are dependent
	np.random.seed = -4
	x = np.random.random(size = num)
	x.sort() 
	y = 2.0 * x 
	z = 0.5 * x * x + 1.5 * x + 3.0 

		#Set up a numpy array adding noise to y and z
	a = np.zeros (shape = (num,3))
	a [:,0 ] = x 
	a [:,1 ] = y + np.random.normal(size = num) 
	a [:,2 ] = z + np.random.normal(size = num) 

		#bin the array according to values of x which is in the col 0
		#using uniform size bins from 0. to 1. of size 0.1
	binnedarray  = nbinarray ( a, 
		binningcol = 0, 
		binmin = 0., 
		binmax = 1.0, 
		binsize = 0.1)

	print binnedarray 
	print type(binnedarray)
	sys.exit()

	print "\n-------------------------\n"
	xbinned=  ngetbinnedvec (binnedarray, 0)
	ybinned=  ngetbinnedvec (binnedarray, 1)
	#print xbinned
	xavg = map (np.average , xbinned)
	yavg = map (np.average , ybinned)
	#xavg =  map( lambda x : np.average(x ) , xbinned )
	#yavg =  map( lambda x : np.average(x) , ybinned)
	#print map( lambda x , w : np.average(x, w), xbinned, ybinned)
	plt.plot(x, y, 'k-')
	plt.plot(a[:,0] , a[:,1], 'ks')
	plt.plot(a[:,0], a[:,2], 'ro')
	plt.plot(x,z , 'r--')
	plt.plot( xavg, yavg, 'bd')
	plt.show()
	
