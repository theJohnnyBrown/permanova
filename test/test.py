#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 - 2012, University of New Orleans
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#

import sys,os
import numpy as np
import cPickle as cp

sys.path.append("../")
sys.path.append(".")
import permanova

TD = "./test_data"

mapping = open(os.path.join(TD,"cross_TV_BV_map.txt")).readlines()
headers = mapping[0].strip().split("\t")
tvi = headers.index("TVstatus")
tv_levels = [r.strip().split('\t')[tvi] for r in mapping[1:]]

#FOOLISH ASSUMPTION: Mapping file has same ordering as dm file. True here
#Output from QIIME is used, these results can be compared to similar analyses
#in QIIME
dmf = open(os.path.join(TD,"unweighted_unifrac_otu_table.txt")).readlines()
dm = np.asarray([map(float,r.strip().split("\t")[1:]) for r in dmf[1:]])

#expected: (4.6822758256772135, p), where p is not significant (likely 0 for 
#any reasonable number of permutations)
print permanova.permanova_oneway(dm,tv_levels)

#example problem taken from
#http://people.richland.edu/james/lecture/m170/ch13-2wy.html
jones_levels = cp.load(open(os.path.join(TD,"jones_levels.cpk")))
jones_dm = cp.load(open(os.path.join(TD,"jones_dm.cpk")))

#see http://people.richland.edu/james/lecture/m170/ch13-2wy.html for 
#expected results. Permutations=10000 should approach accuracy
print permanova.permanova_twoway(jones_dm, jones_levels)
