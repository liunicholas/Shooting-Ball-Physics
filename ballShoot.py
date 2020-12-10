from graphics import *

'''
change variables here:
'''
initialVelocity = 20 #m/s
initialAngle = 30 #degrees
mass = 4 #kilograms
timeInterval = 0.1 #seconds


width = 1300
height = 800
origin = Point(100,100)
xAxisEnd = Point(1150,origin.getY())
yAxisEnd = Point(origin.getX(),700)
gw = GraphWin("ball trajectory", width, height)
gw.setCoords(0,0,width,height)
gw.setBackground("black")

xCoords = []
yCoords = []
xVelocites = []
yVelocities = []
velocities = []
xForces = []
yForces = []
forces = []
times = []

def makeText(text,x,y,color,size,font):
    text = Text(Point(x,y), text)
    text.setFill("white")
    text.setSize(36)
    text.setFace("arial")
    text.draw(gw)

def makeWindowDetails():
    makeText("2D Kinematics With Air Resistance",300,750,"white",36,"arial")

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

def displayPoints():

    return

def main():
    makeWindowDetails()

    click = gw.getMouse()
    gw.close()

main()
