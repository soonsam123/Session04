import lib601.sm as sm
import lib601.util as util
class LTISM(sm.SM):
    def __init__(self, dCoeffs, cCoeffs):
        self.j = len(dCoeffs) - 1
        self.k = len(cCoeffs)
        self.dCoeffs = dCoeffs
        self.cCoeffs = cCoeffs
        # A list with the j previous inputs and the k previous outputs.
        # Start at rest.
        self.startState = ([0.0]*j, [0.0]*k)
    def getNextValues(self, state, input):
        (inputs, outputs) = state
        inputs = [input] + inputs
        currentOutput = util.dotProd(outputs, self.cCoeffs) + \
                        util.dotProd(inputs, self.dCoeffs)
        # list[:-1] is the whole list minus the las element.
        # I take off the last element because it is the oldest.
        return ((inputs[:-1], ([currentOutput] + outputs)[:-1]), currentOutput)
