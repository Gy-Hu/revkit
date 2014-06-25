#!/usr/bin/python
from revkit import *

circ = circuit ()
spec = binary_truth_table ()
read_specification ( spec, "function.spec" )

r = transformation_based_synthesis ( circ, spec )

if type(r) == dict:
  print circ
  print "Runtime: ", r["runtime"], "seconds."
else:
  print r
