#!/usr/bin/env python
import numpy as np


def frequencyofints(a ) :
	
	"""
	find the frequency of integers in an integer array a

	args:
		a : integer array, mandatory
	returns:
		tuple (vals, freq ) where vals are unique integers
		in the array a, and freq is a tuple of frequencies with 
		which the integers occur in each dimension.
	status: 
		tested , R. Biswas, Sun May 11 23:14:39 CDT 2014
		tests in test_sorting.py			
	example_usage:
		>>> z = np.array([1,3,4,2,5,2,3])
		>>> val, freq =  su.frequencyofints(z) 
	"""
	x  = np.bincount(a) 
	vals  = np.nonzero(x) [0]

	freq = x[y]
	return vals, freq 
def findcommonsortedLists(A ,  B , 
	commononly= True, 
	inAnotB =None, 
	both = None, 
	returnelements = True):
	
	"""
	Fast method of finding common numbers in presorted (ascending) 
	iterables A and B with unique elements, as well as elements in 
	A that are not in B or vice-versa.
	args:

	returns:

	Status: 
		
	Notes:
		This should be used for large presorted lists/iterable 
		where ordering is used to find such elements faster than 
		more general methods.

	Assumptions
	A and B are iterables that can be indexed by A[i] and have unique 
	float entries that are pre-sorted to be in ascending order. 
	
	"""
	
	inA = []
	inB = []
	CA   = []
	CB = [] 
	indA = 0 
	indB = 0
    
	lenA = len(A)
	lenB = len(B)
	
	while indA < lenA and indB < lenB :
		
		if A[indA] > B[indB]:
            
			inB.append(indB)
			indB += 1
	   
		elif A[indA] < B[indB]:
			
			inA.append(indA)
			indA += 1
		
		elif A[indA] == B[indB]:
			
			CA.append(indA)
			CB.append(indB)
			indA += 1
			indB += 1
		
		else :
			raise ValueError("How is that possible with", 
				"integers?\n")
		
	for i in range(indA , lenA -1):
		inA.append(indA)

	for i in range(indB , lenB -1 ):
		inB.append(indB)
		
		
	if returnelements:
		rA = A[inA]
		rB = B[inB] 
		rC = A[CA] 
		
	return rA, rB , rC 


if __name__ == "__main__":

	pass
