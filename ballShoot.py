from graphics import *

def makeWindow():
    width = 1200
    height = 800
    gw = GraphWin("ball trajectory", width, height)
    gw.setCoords(0,0,width,height)
    gw.setBackground("black")

    text = Text(Point(80,780), "2D Kinematics With Air Resistance")
    text.setFill("white")
    text.setSize(20)
    text.draw(gw)

    return gw

def main():

    gw = makeWindow()

    click = gw.getMouse()
    gw.close()

main()
