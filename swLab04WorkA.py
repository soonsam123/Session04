import lib601.poly as poly
import lib601.sig
from lib601.sig import *

## You can evaluate expressions that use any of the classes or
## functions from the sig module (Signals class, etc.).  You do not
## need to prefix them with "sig."
class ConstantSignal(Signal):
    def __init__(self, c):
        self.c = c
    def sample(self, n):
        return self.c
    
class CosineSignal(Signal):
    # omega = frequency
    # phase = phase in radians
    def __init__(self, omega = 1, phase = 0):
        self.omega = omega
        self.phase = phase
    def sample(self, n):
        return math.cos(self.omega * n + self.phase)
    
class UnitSampleSignal(Signal):
    def sample(self, n):
        if n == 0:
            return 1
        else:
            return 0
# s = UnitSampleSignal()
# cos = CosineSignal(1,math.pi/2)
# self.plot(start, end, NameofWin, Color of the plots)
# cos.plot(-5,5, 'Cossine', 'yellow')

# *************Five subclasses of Signal******************
# StepSignal() = n <= 0 --> 0, otherwise --> 1
# SummedSignal(s1, s2)
# ScaledSignal(s, c) = Signal s multiplyied by constant c.
# R(s) = Sign s Delayed my one time step.
# Rn(s, n) = Sign s Delayes by n time steps.
# polyR(s, p) = A sign and an instance of poly.Polynomial(c) [c = list of numbers].
# Note that the variable for polyR will be Delay(R).

# Example for polyR.
# p = poly.Polynomial([7,0,1])
# new_s = polyR(s, p)
# new_s.plot(-5,5)

# y1 = StepSignal()
# y2 = s
# y3 = SummedSignal(y1, y2)
# poly = poly.Polynomial([1, 2, 1])
# final = polyR(y3, poly)
# final.plot(-5, 5)

# *****************************WK.4.1.1****************************
# 3R^3Y (Y = Scaled Signal)
step1 = polyR(ScaledSignal(StepSignal(), 3), poly.Polynomial([1,0,0,0]))
step1.plot(-5, 10)
# -3R^7Y (Y = Scaled Signal)
step2 = polyR(ScaledSignal(StepSignal(), -3), poly.Polynomial([1,0,0,0,0,0,0,0]))
step2.plot(-5,10)
# -3R^7Y + 3R^3Y (Y = Scaled Signal)
stepUpDown = SummedSignal(step1, step2)
stepUpDown.plot(-5,10)
# 5R^5X+ 3R^3X+ RX (X = UnitSampleSignal)
stepUpDownPoly_1 = polyR(UnitSampleSignal(), poly.Polynomial([1,0]))
stepUpDownPoly_3 = polyR(UnitSampleSignal(), poly.Polynomial([3,0,0,0]))
stepUpDownPoly_5 = polyR(UnitSampleSignal(), poly.Polynomial([5,0,0,0,0,0]))
stepUpDownPoly = SummedSignal(SummedSignal(stepUpDownPoly_1, stepUpDownPoly_3), stepUpDownPoly_5)
stepUpDownPoly.plot(-5,10)
# The testing for this problem and subsequent ones will use the following function.
def samplesInRange(signal, lo, hi):
    return [signal.sample(i) for i in range(lo, hi)]
usamp = UnitSampleSignal()
polyR(usamp, poly.Polynomial([3, 5, -1, 0, 0, 3, -2])).plot(-5, 15)
