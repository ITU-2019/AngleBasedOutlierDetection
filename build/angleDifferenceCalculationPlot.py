from math import log, floor, sqrt
import numpy as np
import matplotlib.pyplot as plt
from fjlt import *
from Trigonomity import *


def printKValues(e,n):
  k1 = 4/((((e**2)/2)-((e**3)/3)))* log(n) # Simple proofOur paper. 
  k2 = 9/((((e**2))-(2*(e**3)/3)))* log(n) #
  k3 = (e**-2)*log(n)
  k4 = log(n) / (e**2 * log(1 / e))
  return floor(k4) + 1

def printE(elements,dims,reduceddims, q, e):

  beforeAngles = []
  afterAngles = []
  maxAfterAngles = []
  minAfterAngles = []

  mu = 584
  sigma = 3.2


  a =  np.random.normal(mu,sigma,(elements,dims))
  res = fjlt(a.transpose(),reduceddims, q).transpose()
  for i in range(0, elements -2 ):
    j = i + 1
    k = i + 2
    beforeAngle = getAngle(a[i],a[j],a[k])
    afterAngle  = getAngle(res[i],res[j],res[k])

    distA = np.linalg.norm(a[j]-a[k])
    distB = np.linalg.norm(a[i]-a[j])
    distC = np.linalg.norm(a[i]-a[k])

    distAL = sqrt((distA**2)*(1+e))
    distBL = sqrt((distB**2)*(1+e))
    distCL = sqrt((distC**2)*(1+e))

    distAS = sqrt((distA**2)*(1-e))
    distBS = sqrt((distB**2)*(1-e))
    distCS = sqrt((distC**2)*(1-e))
    
    beforeAngles.append(beforeAngle)
    afterAngles.append(afterAngle)

    maxAfterAngles.append(getAngle2(distAL,distBS,distCS))
    minAfterAngles.append(getAngle2(distAS,distBL,distCL))


  afterAngles =    [x for _,x in sorted(zip(beforeAngles,afterAngles))]
  maxAfterAngles = [x for _,x in sorted(zip(beforeAngles,maxAfterAngles))]
  minAfterAngles = [x for _,x in sorted(zip(beforeAngles,minAfterAngles))]
  beforeAngles = sorted(beforeAngles)
  
  plt.plot(afterAngles,"bo", alpha=0.25, markerSize=2, label= "afterPoints")    
  plt.plot(afterAngles, alpha=0.25, label= "afterLines")
  plt.plot(maxAfterAngles, alpha=0.7, label= "maxafter") 
  plt.plot(minAfterAngles, alpha=0.7, label= "minafter") 
  plt.plot(beforeAngles, alpha=0.7, label="before")
  plt.legend(loc='upper left')  
  plt.show()


individuals = 10000
e = 0.3
k = printKValues(e,individuals)
printE(individuals,10,k, 0.9, e)

