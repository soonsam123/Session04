# Name: Soon Sam R Santos
# Date: February 03, 2017
# Session: 4
# Transduced_signals.py

import lib601.sm as sm
import lib601.sig as sig
# import my other py file (This is in this same repository)
import LTISM as l
# Any changes in LTISM will be reloaded here.
reload(l)

# Part 1) Implementation
# Proccedure to check the values in IDLE.
def samplesInRange(sig, lo, hi):
    return [sig.sample(i) for i in range(lo,hi)]

# Sequence of outputs generated by the machine when the original signal is used as an input.

class TransducedSignal(sig.Signal):
    def __init__(self, s, m):
        # s = the inp signal (instance of signal)
        # m = the state machine which will take s as input (instace of SM)
        self.s = s
        self.m = m
    def sample(self, n):
        # This only works for n greater than 0.
        if n < 0:
            return 0
        else:
            self.m.start()
            # The input is the value of the signal at time n.
            return self.m.step(self.s.sample(n))

# TestCases
print samplesInRange(TransducedSignal(sig.StepSignal(), sm.Gain(3)), -5, 10)
# At the steps greater than0, the values should be 3, because the input is 1 (from the signal)
# to the Gain(3) machine --> 3.
print samplesInRange(TransducedSignal(sig.ScaledSignal(sig.StepSignal(), 3), sm.Gain(3)), -5, 10)
# (0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
# Working!

# Part 2) Application
class BankSignal(sig.Signal):
    def sample(self, n):
        if n == 0:
            return 100
        elif n == 20:
            return 100
        elif n == 50:
            return 100
        else:
            return 0
# LTISM representing the bank account: y[n] = x[n] + 1.01 y[n - 1]
