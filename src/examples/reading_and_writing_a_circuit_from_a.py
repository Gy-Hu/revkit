#!/usr/bin/python
from revkit import *

circ = circuit ()
read_realization ( circ, "circuit.real")
reverse_circuit ( circ )
write_realization ( circ, "circuit-copy.real")
