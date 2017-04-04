import lib601.sm as sm

#************Tutor Problem Wk.4.2.1****************
# Part 1)
# y[n] = x[n] + y[n - 1]
S1 = sm.FeedbackAdd(sm.Gain(1),sm.R(0))
print S1.transduce([1,2,3,4,5,6,7,8,9,10])
# Part 2)
# y[n] = x[n - 1] + y[n]
S2 = sm.FeedbackAdd(sm.R(0), sm.Gain(1))
print S2.transduce([1,2,3,4,5,6,7,8,9,10])
# Part 3)
# y[n] = 0.1x[n - 1] + y[n]
# Easier to write from the block diagram.
S3 = sm.Cascade(sm.Gain(0.1), sm.FeedbackAdd(sm.R(0), sm.Gain(1)))
print S3.transduce([1,2,3,4,5,6,7,8,9,10])

#***********Tutor Problem Wk.4.3.3****************
# Part 1)
def accumulator(init):
# init = the output before the first input
    return sm.FeedbackAdd(sm.Gain(1), sm.R(init))
print accumulator(10).transduce([1,2,3,4,5,6,7,8,9,10])
# 65

# Part 2)
def accumulatorDelay(init):
# init = the output at time 0.
    return sm.FeedbackAdd(sm.R(init), sm.Gain(1))
print accumulatorDelay(17).transduce([1,2,3,4,5,6,7,8,9,10])

# Part 3)
def accumulatorDelayScaled(s, init):
# s = the scaled factor.
# init = the output at time 0.
    return sm.Cascade(sm.Gain(s), sm.FeedbackAdd(sm.R(init), sm.Gain(1)))
print accumulatorDelayScaled(0.1, 0).transduce([1,2,3,4,5,6,7,8,9,10,11])

# Procedures are useful because I'll not need to write the whole thing all the times.
