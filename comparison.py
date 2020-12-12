from graphics import *
import math
from time import sleep

'''
change variables here:
'''
initialVelocity = 20 #m/s
initialAngle = 30 #degrees
mass = 4 #kilograms
timeInterval = 0.01 #seconds
k = 2 #combination of drag coefficient, cross sectional area, and density of fluid

width = 1300
height = 800
origin = Point(100,100)
xAxisEnd = Point(1150,100)
yAxisEnd = Point(100,700)
gw = GraphWin("ball trajectory", width, height)
gw.setCoords(0,0,width,height)
gw.setBackground("black")

def makeText(text,x,y,color,size,font):
    text = Text(Point(x,y), text)
    text.setFill("white")
    text.setSize(36)
    text.setFace("arial")
    text.draw(gw)

    return text

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
    xNow = 0
    yNow = 0
    vXNow = math.cos(math.radians(initialAngle))*initialVelocity
    vYNow = math.sin(math.radians(initialAngle))*initialVelocity

    angles = [initialAngle]
    xCoords = [xNow]
    yCoords = [yNow]
    xVelocities = [vXNow]
    yVelocities = [vYNow]
    # velocities = [initialVelocity]
    xForces = [math.cos(math.radians(initialAngle))*(math.pow(initialVelocity,2)*k*-1)]
    yForces = [-9.8*mass+math.sin(math.radians(initialAngle))*(math.pow(initialVelocity,2)*k*-1)]
    # forces = [math.sqrt(math.pow(math.pow(vXNow,2)*k,2)+math.pow(math.pow(vYNow,2)*k,2))]
    times = [0]

    return xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times

def getPointsHeldt(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times):
    timeCounter = 0
    while yNow >= 0:
        vXNow, vYNow = getVectorVelocityHeldt(vXNow, vYNow, xForces, yForces)

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

def getVectorVelocityHeldt(vXNow, vYNow, xForces, yForces):

    force = math.pow(vXNow,2)*k*-1

    xForces.append(force)
    yForces.append(-9.8*mass)

    vXNow += force/mass*timeInterval

    vYNow += -9.8*timeInterval

    return vXNow, vYNow

def getPointsAR(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times):
    timeCounter = 0
    while yNow >= 0:
        vXNow, vYNow = getVectorVelocityAR(vXNow, vYNow, xForces, yForces)

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
    angle = math.atan(vYNow/vXNow)

    force = math.pow(vXNow,2)*k*-1
    xForce = force*math.cos(angle)
    yForce = -9.8*mass+force*math.sin(angle)

    xForces.append(xForce)
    yForces.append(yForce)

    vXNow += xForce/mass*timeInterval

    vYNow += yForce/mass*timeInterval

    return vXNow, vYNow

def getPointsIdeal(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times):
    timeCounter = 0
    while yNow >= 0:
        vXNow, vYNow = getVectorVelocityIdeal(vXNow, vYNow, xForces, yForces)

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
    angle = math.atan(vYNow/vXNow)

    xForce = 0
    yForce = -9.8*mass

    xForces.append(xForce)
    yForces.append(yForce)

    vXNow += xForce/mass*timeInterval

    vYNow += yForce/mass*timeInterval

    return vXNow, vYNow

def findScalingNumber(xCoords, yCoords):
    maxX = max(xCoords)
    maxY = max(yCoords)

    pixelPerX = 1050/maxX
    pixelPerY = 600/maxY

    scale = min([pixelPerX,pixelPerY])

    drawAxes(scale)

    return scale

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

        if i < len(xCoords)-1:
            text2.undraw()
            text3.undraw()
            text4.undraw()
            text5.undraw()
            text6.undraw()

        time.sleep(0.01)

    return

def main():
    makeWindowDetails()

    xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times = makeVars()

    xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times = getPoints(xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times)

    scale = findScalingNumber(xCoords, yCoords)

    displayPoints("red", xNow, yNow, vXNow, vYNow, angles, xCoords, yCoords, xVelocities, yVelocities, xForces, yForces, times, scale)

    while True:
        key = gw.checkKey()
        if key != "":
            gw.close()
            break

main()
