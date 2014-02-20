#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def settwopanel( height_ratios = [1.0,0.3], 
	width_ratios = [1.,0.] ,
	padding = None, 
	figsize  = None ):

	"""
	returns 
	args:
		height_ratios:

		width_ratios :
		
		figsize: 

	returns:

	usage:

	"""

	hpad  = 0.0 
	fig = plt.figure()
	gs = gridspec.GridSpec ( 2, 1, width_ratios = width_ratios , height_ratios = height_ratios)

	ax0 = plt.subplot(gs[0]) 
	ax1 = plt.subplot(gs[1])

	
	gridspec.update(hpad = hpad)
	return fig , ax0 , ax1


if __name__ == "__main__":


	x = np.arange(0,10,0.1)
	y = x * x

	
	myfig,  myax0 , myax1 = settwopanel ( )

	myax0.plot( x,  y) 
	myax1.plot(x, x)
	
	myfig.tight_layout()
	plt.show()
