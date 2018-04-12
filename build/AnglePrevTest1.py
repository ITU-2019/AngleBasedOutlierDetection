from math import log, floor, sqrt
import numpy as np
import matplotlib.pyplot as plt
from fjlt import *
from Trigonomity import *

plt.style.use('ggplot')


def printKValues(e,n):
  k1 = (log(n) * 4) / (((e**2)/2)-((e**3)/3)) # Simple proofOur paper. 
  k2 = 9/((((e**2))-(2*(e**3)/3)))* log(n) #
  k3 = (e**-2)*log(n)
  k4 = log(n) / (e**2 * log(1 / e))
  return floor(k1) + 1



def compareAllAngles(elements,dims,reduceddims, q, e):

  beforeAngles = []
  afterAngles = []
  maxAfterAngles = []
  minAfterAngles = []


  randomCube = np.random.rand(elements,dims)

  broken = 0

  a = randomCube
  res = fjlt(a.transpose(),reduceddims, q).transpose()

  for i in range(0, elements - 2):
    for j in range(i + 1, elements - 1):
      for k in range(j + 1, elements):
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
        maxAfter = getAngle2(distAL,distBS,distCS)
        minAfter = getAngle2(distAS,distBL,distCL)
        maxAfterAngles.append(maxAfter)
        minAfterAngles.append(minAfter)
        if(afterAngle > maxAfter or afterAngle < minAfter):
          broken = broken + 1


  afterAngles =    [x for _,x in sorted(zip(beforeAngles,afterAngles))]
  maxAfterAngles = [x for _,x in sorted(zip(beforeAngles,maxAfterAngles))]
  minAfterAngles = [x for _,x in sorted(zip(beforeAngles,minAfterAngles))]
  beforeAngles = sorted(beforeAngles)

  print(broken)

  plt.plot(afterAngles,"bo", alpha=0.25, markerSize=2,color="blue")    
  plt.plot(afterAngles, alpha=0.25, label= "after angle",color="purple")
  plt.plot(maxAfterAngles, alpha=0.7, label= "max after",color="red") 
  plt.plot(minAfterAngles, alpha=0.7, label= "min after",color="red") 
  plt.plot(beforeAngles, alpha=0.7, label="before",color="black")
  plt.ylim(ymin = 0)
  _,ymax = plt.ylim()
  plt.ylim(ymax = ymax + 10)
  plt.legend(loc='upper left')  
  plt.show()


individuals = 100
e = 0.5
k = printKValues(e,individuals)
print(k)
compareAllAngles(individuals,1000,k, 0.9, e)

