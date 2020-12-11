from graphics import *
import math

'''
change variables here:
'''
initialVelocity = 20 #m/s
initialAngle = 30 #degrees
mass = 4 #kilograms
timeInterval = 0.1 #seconds
k = 2 #combination of drag coefficient, cross sectional area, and density of fluid

width = 1300
height = 800
origin = Point(100,100)
xAxisEnd = Point(1150,100)
yAxisEnd = Point(100,700)
gw = GraphWin("ball trajectory", width, height)
gw.setCoords(0,0,width,height)
gw.setBackground("black")

xNow = 0
yNow = 0
vXNow = math.cos(math.radians(initialAngle))*initialVelocity
vYNow = math.sin(math.radians(initialAngle))*initialVelocity

xCoords = [xNow]
yCoords = [yNow]
xVelocites = [vXNow]
yVelocities = [vYNow]
velocities = [math.sqrt(math.pow(vXNow,2)+math.pow(vYNow,2))]
xForces = [math.pow(vXNow,2)*k]
yForces = [math.pow(vYNow,2)*k]
forces = [math.sqrt(math.pow(math.pow(vXNow,2)*k,2)+math.pow(math.pow(vYNow,2)*k,2))]
times = [0]

def makeText(text,x,y,color,size,font):
    text = Text(Point(x,y), text)
    text.setFill("white")
    text.setSize(36)
    text.setFace("arial")
    text.draw(gw)

def makeWindowDetails():
    makeText("2D Kinematics With Air Resistance",300,750,"white",36,"arial")

    makeText("2D Kinematics With Air Resistance",300,750,"white",36,"arial")
    makeText("Time:",950,800-30,"white",8,"arial")
    makeText("Position:",950,750-30,"white",8,"arial")
    makeText("Velocity:",950,700-30,"white",8,"arial")
    makeText("Force:",950,650-30,"white",8,"arial")
    makeText("Angle:",950,600-30,"white",8,"arial")

    line = Line(origin,xAxisEnd)
    line.setFill("white")
    line.setOutline("white")
    line.draw(gw)

    line = Line(origin,yAxisEnd)
    line.setFill("white")
    line.setOutline("white")
    line.draw(gw)

def getVectorVelocity():

    return

def getVectorForce():

    return

def getPoints():

    return

def findScalingNumber():

    return

def displayPoints():
    for i in range(len(xCoords)):
        point = Point()

    return

def main():
    makeWindowDetails()

    click = gw.getMouse()
    gw.close()

main()
