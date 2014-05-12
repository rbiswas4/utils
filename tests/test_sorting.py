#!/usr/bin/env python

import numpy as np
import utils.sortingutils as su

z = np.array([1,3,4,2,5,2,3])
val, freq =  su.frequencyofints(z) 
print z 
print val
print freq

#assert((array([1, 2, 2, 1, 1]), array([1, 2, 3, 4, 5])))
