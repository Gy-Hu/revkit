#!/usr/bin/python
from revkit import *

spec = binary_truth_table ()
spec.add_entry ( [False, False], [False] )
spec.add_entry ( [False, True ], [False] )
spec.add_entry ( [True , False], [False] )
spec.add_entry ( [True , True ], [True ] )

embed_truth_table ( spec, spec )
circ = circuit ()

r = transformation_based_synthesis ( circ, spec )

if type(r) == dict:
  print circ
  print "Runtime: ", r["runtime"], "seconds."
else:
  print r
