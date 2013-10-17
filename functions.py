#!/usr/bin/env python

import h5py
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

def hdfobj2dict(hdfobj) :

	"""returns 

	"""
	keys = hdfobj.keys()
    
	mydict = {}

	for key in keys:
		mydict[key] = hdfobj[key].value

        return mydict

def hdfobj2df(hdfobj):

	import pandas as pd
	
	mydict = hdfobj2dict(hdfobj)
	tmpdf = pd.DataFrame(mydict)
	df  = tmpdf.sort(column = 'nodeIndex')
	
	return df
   

def loadoutputs(fname ) :

	"""
	"""
	hl = h5py.File(fname, "r") 

		#output slices
	outnames = hl['Outputs'].keys()

	outattr = []
	outs = [] 

	for outname in outnames:
		print outname
			#hdf group 	
		outslices = hl['Outputs'][outname]
		outattr.append(outslices.attrs.items())
		outs.append(hdfobj2df(outslices['nodeData'])) 

	hl.close()

	return outattr , outs 	

if __name__=="__main__":
	
	location = "/Users/rbiswas/doc/projects/galacticus_stuff/"
	galoutfile = location + "/galacticus_big_run_indexed_normal_Planck.hdf5"

	outattr, outs = loadoutputs(galoutfile)

	print outs

	
