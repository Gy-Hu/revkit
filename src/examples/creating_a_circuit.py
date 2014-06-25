#!/usr/bin/python
from revkit import *

circ = circuit( 3 )

append_toffoli( circ, [2], 1 )
append_toffoli( circ, [0, 1], 2 )
append_toffoli( circ, [1, 2], 0 )
append_toffoli( circ, [0, 1], 2 )
append_toffoli( circ, [2], 1 )

print circ
