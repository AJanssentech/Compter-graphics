from grid import Grid

def rasterline(x0, y0, x1, y1):
    g.addPoint(x0,y0)
    g.addPoint(x1,y1)

    deltaX = x1 - x0
    deltaY = y1 - y0 

    if (abs(deltaX) > abs(deltaY)) :
        step = abs(deltaX)
    
    else :
        step = abs(deltaY)
    
    xStep = deltaX / float (step) 
    yStep = deltaY / float (step)

    g.addPoint(round(x0),round(y0),(0,255,255))

    x = x0
    y = y0
    for i in range(step+1) :  
        x = x + xStep
        y = y + yStep
        g.addPoint(round(x),round(y),(0,255,255))

# testcode
# let op: de beoordeling wordt gedaan op basis van andere waarden
g = Grid(20, 20)
rasterline(0, 0, 19, 0)
rasterline(0, 10, 19, 0)
g.draw()
