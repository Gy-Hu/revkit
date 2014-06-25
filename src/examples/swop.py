#!/usr/bin/python
from revkit import *

circ = circuit ()
spec = binary_truth_table ()

counter = 0

read_specification ( spec, "function.spec")

tbs = transformation_based_synthesis_func ( bidirectional = False )

def step():
  global counter
  counter += 1

swop ( circ, spec, synthesis = tbs, stepfunc = swop_step_func.from_callable ( step ))
print counter, "iterations were performed."
