#!/usr/bin/python
import sys
from revkit import *

opts = program_options()
opts.add_read_realization_option()

opts.parse( sys.argv )
if not opts.good():
    print opts
    exit( 1 )

circ = circuit()
read_realization( circ, opts.read_realization_filename() )

for k,v in circ.modules().items():
    print "Circuit %s:" % k
    print_statistics( v )



