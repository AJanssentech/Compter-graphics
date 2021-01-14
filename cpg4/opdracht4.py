#adding libaries
import numpy as np
import math as mt 
from lines import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def calculate () : 
    # making a vector 
    vector = np.array([12,10])
    # making a matrix
    matrix = np.array([[20,40],[10,4]])
    #multiplying the vector and matrix
    result = np.multiply(vector,matrix)
    print(result)

# defineren van de hoekputen 
def hoekpunten () : 
    #making the array with the corner points
    v1 = np.array([-1,-1,-1,1])
    v2 = np.array([1,-1,-1,1])
    v3 = np.array([1,1,-1,1])
    v4 = np.array([-1,1,-1,1])
    v5 = np.array([-1,-1,1,1])
    v6 = np.array([1,-1,1,1])
    v7 = np.array([1,1,1,1])
    v8 = np.array([-1,1,1,1])  
    result = np.array([v1,v2,v3,v4,v5,v6,v7,v8])
    #translatie matrix 
    return result 

def translationMatrix (x,y,z,hoekpuntMatrix) :
    #making the points 
    r1 = np.array([1,0,0,0])
    r2 = np.array([0,1,0,0]) 
    r3 = np.array([0,0,1,0])    
    r4 = np.array([x,y,z,1])
    transMatrix = np.array([r1,r2,r3,r4])
    #multiplying the two matrices with each other
    resultMatrix = np.dot(hoekpuntMatrix,transMatrix)
    return resultMatrix

def scaling (sx,sy,sz,kubusMatrix) :
    # defining a matrixes
    s1 = np.array([sx,0,0,0])
    s2 = np.array([0,sy,0,0])
    s3 = np.array([0,0,sz,0])
    s4 = np.array([0,0,0,1])
    scalingMatrix = np.array([s1,s2,s3,s4])
    #multiplying the matrixes
    resultMatrix = np.dot(kubusMatrix,scalingMatrix)
    #print(resultMatrix)
    return resultMatrix

def rotation(x,y,z,kubusMatrix) :
    # We have to use radiants for the sin in thelibary function
    # making the matrices
    radialenX = mt.radians(x)
    radialenY = mt.radians(y)
    radialenZ = mt.radians(z)
    # x
    xr1 = np.array([1,0,0,0])
    xr2 = np.array([0,mt.cos(x),-mt.sin(radialenX),0])
    xr3 = np.array([0,mt.sin(radialenX),mt.cos(x),0])
    xr4 = np.array([0,0,0,1])
    xRotation = np.array([xr1,xr2,xr3,xr4])
    #y 
    yr1 = np.array([mt.cos(y),0,mt.sin(radialenY),0])
    yr2 = np.array([0,1,0,0])
    yr3 = np.array([-mt.sin(radialenY),0,mt.cos(y),0])
    yr4 = np.array([0,0,0,1])
    yRotation = np.array([yr1,yr2,yr3,yr4])
    #z 
    zr1 = np.array([mt.cos(z), - mt.sin(radialenZ),0,0])
    zr2 = np.array([mt.sin(radialenZ), mt.cos(z),0,0])
    zr3 = np.array([0,0,1,0])
    zr4 = np.array([0,0,0,1])
    zRotation = np.array([zr1,zr2,zr3,zr4])
    # multiplying the arrays
    resultmatrix = np.dot(xRotation,yRotation,zRotation)
    multiplyMatrix = np.dot(kubusMatrix,resultmatrix)
    return multiplyMatrix

#def persepective (kubusmatrix) :
#    translatie van de x en y waarde 
#    z=5

#    pm1 = np.array([z,0,0,0])
#    pm2 = np.array([0,z,0,0])
#    pm3 = np.array([0,0,z,0])
#    pm4 = np.array([0,0,1,0])
#
#    projectieMatrix = np.array([pm1,pm2,pm3,pm4])    
#
#    result = np.dot(kubusmatrix,projectieMatrix)
#    print(result) 


def isometrisch (kubusMatrix) :
    kubusMatrix = rotation(30,0,0,kubusMatrix)
    kubusMatrix = scaling(50,50,50,kubusMatrix)
    kubusMatrix = translationMatrix(240, 240, 0, kubusMatrix)

    i1 = np.array([(1/mt.sqrt(2)),0,(1/mt.sqrt(2)),0])
    i2 = np.array([(1/mt.sqrt(6)),mt.sqrt(2/3),-(1/mt.sqrt(6)),0])
    isoMatrix = np.array([i1,i2])

    lines = [[0,1],[1,2],[2,3],[3,0],[0,4],[1,5],[2,6],[3,7],[4,5],[5,6],[6,7],[7,4]]

    results = []
    for j in kubusMatrix :
        results.append(np.dot(isoMatrix,j))

    l = Lines(610,480)
    #l.addLine((100,100),(500,300))

    for i in lines : 
        l.addLine((results[i[0]][0], results[i[0]][1]),(results[i[1]][0], results[i[1]][1]))
    l.draw()

    

def main () :
    result = hoekpunten()
    resultMatrix = translationMatrix(35,40,6,result)
    scaleMatrix = scaling(2,4,6,resultMatrix)
    rotatieMatrix = rotation(5,6,7,scaleMatrix)
    isometrisch(hoekpunten()) 
main()    