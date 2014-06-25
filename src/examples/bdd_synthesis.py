#!/usr/bin/python
from revkit import *

circ = circuit ()
r = bdd_synthesis ( circ, "function.pla", dotfilename = "/tmp/test.dot") 


if type(r) == dict:
  print_statistics( circ, runtime = r["runtime"], main_template = print_statistics_settings().main_template + "Nodes:            " + str( r["node_count"] ) + "\n" )
else:
  print r

