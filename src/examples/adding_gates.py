#!/usr/bin/python
from revkit import *

circ = circuit( 5 )
circ.inputs = [ "i_1", "i_2", "i_3", "i_4", "i_5" ]
circ.outputs = [ "o_1", "o_2", "o_3", "o_4", "o_5" ]

append_cnot( circ, 2, 3 )
prepend_v( circ, 0, 1 )
append_fredkin( circ, [0, 1], 2, 4 )
insert_vplus( circ, 2, 1, 2 )
prepend_not( circ, 2 )
append_toffoli( circ, [0, 1, 2, 3], 4 )

print create_image( circ, elem_width = 0.75 )
