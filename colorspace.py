def RGBtoCMY(r, g, b):
    c = 1 - r
    m = 1 - g 
    y = 1 - b 
    return c, m, y

def CMYtoRGB(c, m, y):
    r = 1 - c 
    g = 1 - m
    b = 1 - y
    return r, g, b

def RGBtoHSL(r, g, b):
    cMin = min(r,g,b) 
    cMax = max(r,g,b)

    deltaC = cMax - cMin
    addC = cMax + cMin 
    
    if cMax == cMin : 
        h = 0 
    elif cMax == r : 
        h = (60 * (g-b)/deltaC + 360)
    elif cMax == g : 
        h =  (60 * (b-r)/deltaC + 360)
    elif cMax == b : 
        h = (60 * (r-g)/deltaC+240 )

    s = deltaC / (1 - (abs(addC)-1))
    l = (addC / 2)
    
    return h, round(s,1), l
     
    
def HSLtoRGB(h, s, l):
    
    r = calculate(h - 120, s, l) 
    g = calculate(h + 120, s, l) 
    b = calculate(h, s, l)

    return round(r,3), g, round(b,1)

def calculate(h, s, l): 
    b = 0.0
    cMin = l + s * abs(l-0.5) - 0.5*s
    cMax = l - s * abs(l-0.5) + 0.5*s

    deltaC = cMax - cMin
    modH = h%360

    if 0 <= modH < 120 :
        b = cMin
    elif 120 <= modH < 180 :
        b = cMin + deltaC * ((modH - 120) / 60)
    elif 180 <= modH < 300 :
        b = cMax
    elif 300 <= modH < 360 : 
        b = cMax - deltaC * ((modH - 300) / 60) 
    return b      




def transparency(r1, g1, b1, alpha, r2, g2, b2):
    r = r1 * alpha + r2 * (1 - alpha)
    b = b1 * alpha + b2 * (1 - alpha)
    g = g1 * alpha + g2 * (1 - alpha)
    return r, round(g,2), b



def printAnswer(): 
    print(RGBtoCMY(0.4, 0.5, 0.6)) # (0.6, 0.5, 0.4)
    print(CMYtoRGB(0.4, 0.5, 0.6)) # (0.6, 0.5, 0.4)      
    print(RGBtoHSL(0.4, 0.5, 0.6)) # (210.0, 0.2, 0.5)
    print(HSLtoRGB(100, 0.5, 0.6)) # (0.533, 0.8, 0.4)
    print(transparency(0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)) # (0.52, 0.62, 0.72) 

printAnswer()
    



