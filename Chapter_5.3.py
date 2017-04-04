# Name: Soon Sam R Santos
# Date: March 10, 2017
# Session: 3
# Chapter_5.3.py
import lib601.sm as sm
m1 = sm.Cascade(sm.Gain(-1), sm.Delay(3))
print m1.transduce([10])

m2 = sm.Cascade(sm.ParallelAdd(sm.Wire(), sm.Cascade(sm.Gain(-1), sm.R(2))), sm.R(3))
print m2.transduce([1,0])
# Cascade machines: The output of the first one is the input of the second one.
print "------------------------------------" # Organazing
d1 = 0
d3 = 3
d2 = 2
# d2 must be equal 2
# d1 d3 can be any value since d1 + d3 = 3
M1 = sm.Cascade(sm.ParallelAdd(sm.Wire(), sm.Cascade(sm.Gain(-1), sm.Delay(2))), sm.Delay(3))
M2 = sm.ParallelAdd(sm.Delay(d1), sm.Cascade(sm.Gain(-1), sm.Cascade(sm.Delay(d2), sm.Delay(d3))))
print M1.transduce([1,0,0,0])
print M2.transduce([1,0,0,0])
# Both outputs are the same
# [3, 3, -1, 0]
# After the thrid time step, the machine does not depend anymore on d1, d2 or d3,
# and any input for both machines will generate the same output.
