from math import log, floor, sqrt
import numpy as np
import matplotlib.pyplot as plt
from fjlt import *
from Trigonomity import *

plt.style.use('ggplot')


def genMinMaxAngle(a,b,c,e):
    distAL = sqrt((a**2)*(1+e))
    distBL = sqrt((b**2)*(1+e))
    distCL = sqrt((c**2)*(1+e))
    distAS = sqrt((a**2)*(1-e))
    distBS = sqrt((b**2)*(1-e))
    distCS = sqrt((c**2)*(1-e))
    return (getAngle2(distAL,distBS,distCS) , getAngle2(distAS,distBL,distCL))

def makeGraph():

  beforeAngles = []
  afterAngles = []
  maxAfterAngles01 = []
  minAfterAngles01 = []
  maxAfterAngles05 = []
  minAfterAngles05 = []
  maxAfterAngles09 = []
  minAfterAngles09 = []

  for i in range(0, 80):
    a = i/100.
    b = 1.-i/100.
    c = 1.-i/100. 
    beforeAngle = getAngle2(a,b,c)
    beforeAngles.append(beforeAngle)

    (maxAngle01, minAngle01) = genMinMaxAngle(a,b,c,0.1)
    (maxAngle05, minAngle05) = genMinMaxAngle(a,b,c,0.5)
    (maxAngle09, minAngle09) = genMinMaxAngle(a,b,c,0.9)

    maxAfterAngles01.append(maxAngle01)
    minAfterAngles01.append(minAngle01)
    maxAfterAngles05.append(maxAngle05)
    minAfterAngles05.append(minAngle05)
    maxAfterAngles09.append(maxAngle09)
    minAfterAngles09.append(minAngle09)


  plt.plot(maxAfterAngles01, alpha=0.7, label= "maxafter e = 0.1") 
  plt.plot(minAfterAngles01, alpha=0.7, label= "minafter e = 0.1") 
  plt.plot(maxAfterAngles05, alpha=0.7, label= "maxafter e = 0.5") 
  plt.plot(minAfterAngles05, alpha=0.7, label= "minafter e = 0.5")   
  plt.plot(maxAfterAngles09, alpha=0.7, label= "maxafter e = 0.9") 
  plt.plot(minAfterAngles09, alpha=0.7, label= "minafter e = 0.9") 
  plt.plot(beforeAngles, alpha=0.7, label="before")

  ymin,ymax = plt.ylim()
  plt.yticks(np.arange(0, 180.01, 15))
  plt.xticks(np.arange(0, 80, 81))
  plt.ylabel("angle")
  plt.legend(loc='upper left')  
  plt.show()


makeGraph()

