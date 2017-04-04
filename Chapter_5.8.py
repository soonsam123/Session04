# Name: Soon Sam R Santos
# Date: March 13, 2017
# Session: 4
# Chapter_5.8.py
import math
import lib601.sm as sm
class Thing(sm.SM):
    startState = [0,0,0,0]
    def getNextValues(self, state, inp):
        # 2 * the output delayed by two time steps plus 3 * the input delayed by two time steps.
        result = state[0] * 2 + state[2] * 3
        newState = [state[1], result, state[3], inp]
        return (newState, result)
print Thing().transduce([1,2,0,1,3])
# [0, 0, 3, 6, 6]

# Trying to do the same thing with the state machines I already know.
print sm.FeedbackAdd(sm.Cascade(sm.Gain(3), sm.Cascade(sm.R(0), sm.R(0))), sm.Cascade(sm.Gain(3), sm.Cascade(sm.R(0), sm.R(0)))).transduce([1,2,0,1,3,0,0], verbose=True)
print sm.ParallelAdd(sm.Cascade(sm.Gain(3), sm.Cascade(sm.R(0), sm.R(0))), sm.Feedback(sm.Cascade(sm.Gain(2), sm.Cascade(sm.R(0), sm.R(0))))).transduce([1,2,0,1,3], verbose=True)
