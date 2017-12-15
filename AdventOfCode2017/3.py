import math

def distanceToCenter(x):
    if x==1: return 0
    circle = math.ceil(x**0.5)//2
    circleSize = circle*2+1
    corner = circleSize**2
    distToCorner = (corner-x)%(circleSize-1)
    distToMidPoint = abs(distToCorner-circleSize//2)
    return circle+distToMidPoint

def partOne():
    print(distanceToCenter(myNumber))

myNumber = 325489
partOne()
