from graphics import *
import math
from time import sleep

'''
change variables here:
'''
# initialVelocity = 20 #m/s
# initialAngle = 30 #degrees
# mass = 2.27 #kilograms
# timeInterval = 0.01 #seconds
# k = 0.406 #combination of drag coefficient, cross sectional area, and density of fluid

initialVelocity = 20 #m/s
initialAngle = 30 #degrees
mass = 0.057 #kilograms
timeInterval = 0.01 #seconds
k = 0.001 #combination of drag coefficient, cross sectional area, and density of fluid

#window details
width = 1300
height = 800
origin = Point(100,100)
xAxisEnd = Point(1150,100)
yAxisEnd = Point(100,700)
gw = GraphWin("ball trajectory", width, height)
gw.setCoords(0,0,width,height)
gw.setBackground("black")

#function for making text
def makeText(text,x,y,color,size,font):
    text = Text(Point(x,y), text)
    text.setFill("white")
    text.setSize(36)
    text.setFace("arial")
    text.draw(gw)

    return text

#functions for drawing
def makeWindowDetails():
    makeText("2D Kinematics With Air Resistance",300,750,"white",36,"arial")

    text = makeText("2D Kinematics With Air Resistance",300,750,"white",36,"arial")
    text = makeText("Time:",950,800-30,"white",6,"arial")
    text = makeText("Position:",950,750-30,"white",6,"arial")
    text = makeText("Velocity:",950,700-30,"white",6,"arial")
    text = makeText("Force:",950,650-30,"white",6,"arial")
    text = makeText("Angle:",950,600-30,"white",6,"arial")
    # makeText("Total X Distance:",950,550-30,"white",8,"arial")

    line = Line(origin,xAxisEnd)
    line.setFill("white")
    line.setOutline("white")
    line.draw(gw)

    line = Line(origin,yAxisEnd)
    line.setFill("white")
    line.setOutline("white")
    line.draw(gw)

def makeVars():
    #initial position
    xNow = 0
    yNow = 0
    #initial velocity
    vXNow = math.cos(math.radians(initialAngle))*initialVelocity
    vYNow = math.sin(math.radians(initialAngle))*initialVelocity

    #lists for graphing later
    angles = [initialAngle]
    xCoords = [xNow]
    yCoords = [yNow]
    xVelocities = [vXNow]
    yVelocities = [vYNow]
    xForces = [math.cos(math.radians(initialAngle))*(math.pow(initialVelocity,2)*k*-1)]
    yForces = [-9.8*mass+math.sin(math.radians(initialAngle))*(math.pow(initialVelocity,2)*k*-1)]
    times = [0]

    return xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times

def getPointsWrong(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times):
    timeCounter = 0
    #loops until the object lands (y<0)
    while yNow >= 0:
        #gets the instantaneous velcity vector components
        vXNow, vYNow = getVectorVelocityWrong(vXNow, vYNow, xForces, yForces)

        #euler's method of changing posiiton using a tangent line at a moment in time
        xNow += vXNow*timeInterval
        yNow += vYNow*timeInterval

        xVelocities.append(vXNow)
        yVelocities.append(vYNow)
        xCoords.append(xNow)
        yCoords.append(yNow)

        angles.append(math.degrees(math.atan(vYNow/vXNow)))

        timeCounter += 1
        times.append(timeCounter*timeInterval)

    return xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times

def getVectorVelocityWrong(vXNow, vYNow, xForces, yForces):
    #force of drag with air resistance formula -kv^2
    force = math.pow(vXNow,2)*k*-1

    #if the drag force was only on the x axis
    xForces.append(force)
    #force from gravity on the x axis
    yForces.append(-9.8*mass)

    #euler's method with force and a small time interval
    vXNow += force/mass*timeInterval
    vYNow += -9.8*timeInterval

    return vXNow, vYNow

def getPointsAR(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times):
    timeCounter = 0
    #loops until the object lands (y<0)
    while yNow >= 0:
        #gets the instantaneous velcity vector components
        vXNow, vYNow = getVectorVelocityAR(vXNow, vYNow, xForces, yForces)

        #euler's method of changing posiiton using a tangent line at a moment in time
        xNow += vXNow*timeInterval
        yNow += vYNow*timeInterval

        xVelocities.append(vXNow)
        yVelocities.append(vYNow)
        xCoords.append(xNow)
        yCoords.append(yNow)

        angles.append(math.degrees(math.atan(vYNow/vXNow)))

        timeCounter += 1
        times.append(timeCounter*timeInterval)

    return xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times

def getVectorVelocityAR(vXNow, vYNow, xForces, yForces):
    #angle for changing the magntiude of the force to the individual vectors
    angle = math.atan(vYNow/vXNow)

    #force of drag with air resistance formula -kv^2
    force = math.pow(vXNow,2)*k*-1

    #drag x component
    xForce = force*math.cos(angle)
    #drag y component plus gravity
    yForce = -9.8*mass+force*math.sin(angle)

    xForces.append(xForce)
    yForces.append(yForce)

    #euler's method with force and a small time interval
    vXNow += xForce/mass*timeInterval
    vYNow += yForce/mass*timeInterval

    return vXNow, vYNow

def getPointsIdeal(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times):
    timeCounter = 0
    #loops until the object lands (y<0)
    while yNow >= 0:
        #gets the instantaneous velcity vector components
        vXNow, vYNow = getVectorVelocityIdeal(vXNow, vYNow, xForces, yForces)

        #euler's method of changing posiiton using a tangent line at a moment in time
        xNow += vXNow*timeInterval
        yNow += vYNow*timeInterval

        xVelocities.append(vXNow)
        yVelocities.append(vYNow)
        xCoords.append(xNow)
        yCoords.append(yNow)

        angles.append(math.degrees(math.atan(vYNow/vXNow)))

        timeCounter += 1
        times.append(timeCounter*timeInterval)

    return xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times

def getVectorVelocityIdeal(vXNow, vYNow, xForces, yForces):
    #when there's no air resistance, there is no x force on the object
    xForce = 0
    #the only force on the object is gravity
    yForce = -9.8*mass

    xForces.append(xForce)
    yForces.append(yForce)

    #euler's method with force and a small time interval
    vXNow += xForce/mass*timeInterval
    vYNow += yForce/mass*timeInterval

    return vXNow, vYNow

#function to scale the graph based off the distance and heigh the ball travels
def findScalingNumber(xCoords, yCoords):
    maxX = max(xCoords)
    maxY = max(yCoords)

    pixelPerX = 1050/maxX
    pixelPerY = 600/maxY

    scale = min([pixelPerX,pixelPerY])

    drawAxes(scale)

    return scale

#draws proper axes based off the scale of the graph
def drawAxes(scale):
    xD = 1050/15
    for i in range(1,15):
        line = Line(Point(xD*i+100,105),Point(xD*i+100,95))
        line.setFill("white")
        line.setOutline("white")
        line.draw(gw)

        label = xD*i/scale
        text = makeText("%0.1f" % label,xD*i+100,70,"white",1,"arial")

    yD = 700/10
    for i in range(1,9):
        line = Line(Point(95,yD*i+100),Point(105,yD*i+100))
        line.setFill("white")
        line.setOutline("white")
        line.draw(gw)

        label = yD*i/scale
        text = makeText("%0.1f" % label,60,xD*i+100,"white",1,"arial")

#drawing the points
def displayPoints(color, xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times, scale):
    for i in range(len(xCoords)):
        text2 = makeText("%.2f" % times[i],1130,800-30,"white",6,"arial")
        text3 = makeText("(%.2f,%.2f)" % (xCoords[i], yCoords[i]),1130,750-30,"white",6,"arial")
        text4 = makeText("(%.2f,%.2f)" % (xVelocities[i], yVelocities[i]),1130,700-30,"white",6,"arial")
        text5 = makeText("(%.2f,%.2f)" % (xForces[i], yForces[i]),1130,650-30,"white",6,"arial")
        text6 = makeText("%.2f" % angles[i],1130,600-30,"white",6,"arial")

        point = Point(xCoords[i]*scale+100,yCoords[i]*scale+100)
        circle = Circle(point, 3)
        circle.setOutline(color)
        circle.setFill(color)
        circle.draw(gw)

        text2.undraw()
        text3.undraw()
        text4.undraw()
        text5.undraw()
        text6.undraw()

        time.sleep(0.005)

    return

def main():
    #draw the graphing window
    makeWindowDetails()

    #press any key to start the program
    while True:
        key = gw.checkKey()
        if key != "":
            break

    #initiate lists and variables
    xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times = makeVars()
    #find the points for the trajectory of the object (no air resiatnce)
    xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times = getPointsIdeal(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times)
    #find the proper scaling number to display the graph
    scale = findScalingNumber(xCoords, yCoords)
    #display the graph
    displayPoints("red", xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times, scale)

    #initiate lists and variables
    xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times = makeVars()
    #find the points for the trajectory of the object (only applying drag force to x axis)
    xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times = getPointsWrong(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times)
    #display the graph
    displayPoints("yellow", xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times, scale)

    #initiate lists and variables
    xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times = makeVars()
    #find the points for the trajectory of the object (air resistance)
    xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times = getPointsAR(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times)
    #display the graph
    displayPoints("green", xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times, scale)

    #press any key to end the program
    while True:
        key = gw.checkKey()
        if key != "":
            gw.close()
            break

main()
