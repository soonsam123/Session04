import lib601.sm as sm
# Returns the dotproduct of two lists of numbers.
# The lists must be of the same size.
def dotProd(a, b):
    if len(a)==0 or len(b)==0: return 0
    if len(a)!=len(b):
        print 'dotProd mismatch error ' + str(len(a)) + ' != ' + str(len(b))
    return sum([ai*bi for (ai,bi) in zip(a,b)])
class LTISM(sm.SM):
    # y[n] = co.y[n-1] + c1.y[n-2]+...+ck-1.y[n-k] + dox[n] + d1x[n-1]+...+dj.x[n-j]
    def __init__(self, dCoeffs, cCoeffs, previousInputs=[], previousOutputs=[]):
        # do to dj
        self.dCoeffs = dCoeffs
        # co to ck-1
        self.cCoeffs = cCoeffs
        # State is the last j input values and the last k output values.
        self.startState = (previousInputs, previousOutputs)
    def getNextValues(self, state, inp):
        (inputs, outputs) = state
        # The actual inp must be in the beginning of the list
        # because it is the x[0] while the others are x[-1],x[-2]...x[-j]
        inputs = [inp] + inputs
        inp_results = dotProd(self.dCoeffs, inputs) 
        out_results = dotProd(self.cCoeffs, outputs)
        output = inp_results + out_results
        # NextState = (inputs[:-1] = all the inputs, except the last one.
        # [output] + outputs[:-1] = the current output plus all the other ones, except of the last one).
        return ((inputs[:-1], [output] + outputs[:-1]), output)

# TestCase
m = LTISM([1,2], [1], [3], [4])
print m.transduce([1,2,3,4,5])
# [11, 15, 22, 32, 45]
