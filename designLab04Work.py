import lib601.sig  as sig # Signal
import lib601.ts as ts  # TransducedSignal
import lib601.sm as sm  # SM

######################################################################
##  Make a state machine model using primitives and combinators
######################################################################

def plant(T, initD):  # initD = initial actual distance to the wall
    # input = commanded velocity
    # output = actual distance to the wall
    # do[n] = do[n - 1] - Tv[n - 1]
    # -T and FeedbackAdd to adjust the order of the terms in the equation.
    return sm.Cascade(sm.Cascade(sm.Gain(-T), sm.R(0)), sm.FeedbackAdd(sm.Gain(1), sm.R(initD)))
def controller(k):
    # inp = distance error
    # out = commanded velocity
    # v[n] = k.e[n]
    return sm.Gain(k)
def sensor(initD):
    # inp = actual sensor values
    # out = one-step delayed sensor reading
    return sm.R(initD)
def wallFinderSystem(T, initD, k):
    # inp = desired distance
    # out = actual distance
    return sm.FeedbackSubtract(sm.Cascade(controller(k), plant(T, initD)), sensor(initD))

# Plots the sequence of distances when the robot starts at distance
# initD from the wall, and desires to be at distance 0.7 m.  Time step
# is 0.1 s.  Parameter k is the gain;  end specifies how many steps to
# plot. 

initD = 1.5

def plotD(k, end = 50):
  d = ts.TransducedSignal(sig.ConstantSignal(0.7),
                          wallFinderSystem(0.1, initD, k))
  d.plot(0, end, newWindow = 'Gain '+str(k))

Wall = wallFinderSystem(0.1, 1.5, -1)
print Wall.transduce([0.7]*50)
# T = 0.1
# initD = 1.5
# k = -1
# di = 0.7
# These informations are the same for the wallFinderSystem and for the plotD, the only difference
# is the way they are showing the path, one is showing by numbers and the other by signs,
# but both go from 1.5 all the way down to 0.7
# As the robot gets closer to the wall, it's velocity descreases. This is a very smart code.

# The distance converges monotonically (without oscillation)
plotD(-1)
# The distance oscillate and converges (approaches a finit value)
plotD(-7)
# The distance oscillates and diverges (grows without bond)
plotD(3)

