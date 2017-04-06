# Name: Soon Sam R Santos
# Date: April 06, 2017
# Session: 4
# Triangle.py

import lib601.sig as sig

# To test the signals in IDLE.
def samplesInRange(sig, lo, hi):
    return [sig.sample(i) for i in range(lo,hi)]

class Triangle(sig.Signal):
    def __init__(self, h):
        # Height of the triangle.
        self.h = h
    def sample(self, n):
        if -self.h <= n <= self.h:
            return self.h - abs(n)
        else:
            return 0

# TestCases

T = Triangle(5)
print T.samplesInRange(-6, 8)
# [0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 0]
T1 = Triangle(8)
print T1.samplesInRange(-9,8)

# TestCases in IDLE-n.bat
T.plot(-6,8)
T1.plot(-9,8)

