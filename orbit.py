#############################
#
#  Author: Sean Gregor
#
#   Desc: A circle orbits the center
#
#############################

from graphics import *
import math

win = GraphWin("Orbit",500,500)

center = Point(250,250)
radius = 150

thingOrbiting = Circle(Point(350,250), 10)

center.draw(win)
thingOrbiting.draw(win)

sun = Circle(center,radius, "yellow")
sun.draw(win)

def getXCoor(deg):
    xCoor = math.sin(math.radians(deg)) * radius
    return xCoor

def getYCoor(deg):
    YCoor = math.cos(math.radians(deg)) * radius
    return YCoor

degree = 1
while(True):
    if(degree > 360):
        degree = 1
    
    dirX = -(thingOrbiting.getCenter().getX() - (center.getX() + getXCoor(degree)))
    print(dirX)
    dirY = -(thingOrbiting.getCenter().getY() - (center.getY() + getYCoor(degree)))
    print(dirY)

    thingOrbiting.move(dirX, dirY)

    degree += 1
    update(20)

    click = win.checkMouse()
    if(click):
        break
    
    

win.getMouse()
win.close()
