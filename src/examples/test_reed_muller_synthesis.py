#!/usr/bin/python
import glob

from revkit import *

for f in glob.glob( "../../benchmarks/suites/exact_synthesis/*.pla" ):
    spec = binary_truth_table()
    read_pla( spec, f )
    embed_truth_table( spec, spec )

    circ = circuit()
    circ_tbs = circuit()

    reed_muller_synthesis( circ, spec )
    transformation_based_synthesis( circ_tbs, spec )

    print "RMS: %d -- TBS: %d" % ( costs( circ, gate_costs() ), costs( circ_tbs, gate_costs() ) )

    print equivalence_check( circ_tbs, circ )['equivalent']

exit( 0 )

circ = circuit()
spec = binary_truth_table()

read_specification( spec, "test/spectra2.spec" )


circ_tbs = circuit()

reed_muller_synthesis( circ, spec )
transformation_based_synthesis( circ_tbs, spec )

spec2 = binary_truth_table()

#circuit_to_truth_table( circ_tbs, spec2 )

#print spec2

print_circuit( circ, print_inputs_and_outputs = True )

print equivalence_check( circ_tbs, circ )['equivalent']
