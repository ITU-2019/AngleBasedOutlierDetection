from math import log, floor, sqrt
import numpy as np
import matplotlib.pyplot as plt
from fjlt import *
from Trigonomity import *


def printKValues(e,n):
  #k1 = 4/((((e**2)/2)-((e**3)/3)))* log(n) # Simple proofOur paper. 
  #k2 = 9/((((e**2))-(2*(e**3)/3)))* log(n) #
  k3 = (e**-2)*log(n)
  #k4 = log(n) / (e**2 * log(1 / e))
  return floor(k3) + 1

def printE( e):

  beforeAngles = []
  afterAngles = []
  maxAfterAngles = []
  minAfterAngles = []

  for i in range(0, 80):
    a = i/100.
    b = 1.-i/100.
    c = 1.-i/100. 
    beforeAngle = getAngle2(a,b,c)

    distA = a
    distB = b
    distC = c

    distAL = sqrt((distA**2)*(1+e))
    distBL = sqrt((distB**2)*(1+e))
    distCL = sqrt((distC**2)*(1+e))

    distAS = sqrt((distA**2)*(1-e))
    distBS = sqrt((distB**2)*(1-e))
    distCS = sqrt((distC**2)*(1-e))
    
    beforeAngles.append(beforeAngle)

    maxAfterAngles.append(getAngle2(distAL,distBS,distCS))
    minAfterAngles.append(getAngle2(distAS,distBL,distCL))


  #afterAngles =    [x for _,x in sorted(zip(beforeAngles,afterAngles))]
  #maxAfterAngles = [x for _,x in sorted(zip(beforeAngles,maxAfterAngles))]
  #minAfterAngles = [x for _,x in sorted(zip(beforeAngles,minAfterAngles))]
  #beforeAngles = sorted(beforeAngles)
  
  plt.plot(maxAfterAngles, alpha=0.7, label= "maxafter") 
  plt.plot(minAfterAngles, alpha=0.7, label= "minafter") 
  plt.plot(beforeAngles, alpha=0.7, label="before")

  plt.legend(loc='upper left')  
  plt.show()


individuals = 1000
e = 0.5
k = printKValues(e,individuals)
print(k)
printE( e)

