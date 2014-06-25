#!/usr/bin/python
from revkit import *

circ = circuit ()
read_realization ( circ, "circuit.real" )

for g in circ.gates:
  print "Gate has" , g.num_controls , "controls."
