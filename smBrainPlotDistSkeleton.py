import math
import lib601.sm as sm
from soar.io import io
import lib601.gfx as gfx
import lib601.util as util


######################################################################
#
#            Do your work in this file
#
######################################################################

dDesired = 0.7



# Input is output of Sensor machine (below); output is an action.
# Note that this machine must also compute E, the error, and output
# the velocity, based on that.
class Controller(sm.SM):
    def __init__(self, k):
        self.k = k
    def getNextValues(self, state, inp):
        # Calculating the error signal.
        # The second value is the straight distance to the wall,
        # considering a 45 degree angle between inp.sonars[3] and the wall.
        E = dDesired - (math.sin(math.pi/4)*inp)
        vel = self.k*E
        return (state, io.Action(fvel= vel, rvel= 0))
        

# Input is SensorInput instance; output is a delayed front sonar reading 
class Sensor(sm.SM):
    def __init__(self, initDist, numDelays):
        self.startState = [initDist]*numDelays
    def getNextValues(self, state, inp):
        # This is the value of a sonar right in the middle of the robot,
        # the correct distane to the wall.
        print inp.sonars[3]*math.sin(math.pi/4)
        output = state[-1]
        state = [inp.sonars[3]] + state[:-1]
        return (state, output)

mySM = sm.Cascade(Sensor(1.5, 1), Controller(3))
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addStaticPlotFunction(y=('sonar'+str(sonarNum),
                                 lambda: io.SensorInput().sonars[sonarNum]))

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    plotSonar(3)
    robot.behavior = mySM
    robot.behavior.start(traceTasks = robot.gfx.tasks())

def brainStart():
    pass

def step():
    robot.behavior.step(io.SensorInput()).execute()

def brainStop():
    pass

def shutdown():
    pass
