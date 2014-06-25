#!/usr/bin/python
from revkit import *

circ = circuit ()
read_realization ( circ, "circuit.real" )
 
a = init_gui ()

w = display_circuit ( circ )
w.simulate ( [1,0,0] ) 

exit ( a.exec_() )

