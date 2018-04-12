from math import log, floor, sqrt
import numpy as np
import matplotlib.pyplot as plt
from fjlt import *
from Trigonomity import *

plt.style.use('ggplot')


def printKValues(e,n):
  #k1 = 4/((((e**2)/2)-((e**3)/3)))* log(n) # Simple proofOur paper. 
  #k2 = 9/((((e**2))-(2*(e**3)/3)))* log(n) #
  k3 = (e**-2)*log(n)
  #k4 = log(n) / (e**2 * log(1 / e))
  return floor(k3) + 1



def compareAllAngles(elements,dims,reduceddims, q, e):

  beforeAngles = []
  afterAngles = []
  maxAfterAngles = []
  minAfterAngles = []

  outlier = np.full((1, dims),2)
  print(outlier.shape)
  randomSphere = np.random.rand(elements,dims)
  print(randomSphere.shape)

  a = np.append(outlier, randomSphere,axis=0)
  res = fjlt(a.transpose(),reduceddims, q).transpose()
  
  for i in range(1, elements -1 ):
    j = i 
    k = i + 1
    beforeAngle = getAngle(a[0],a[j],a[k])
    afterAngle  = getAngle(res[0],res[j],res[k])

    distA = np.linalg.norm(a[j]-a[k])
    distB = np.linalg.norm(a[0]-a[j])
    distC = np.linalg.norm(a[0]-a[k])

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

  
  plt.plot(afterAngles,"bo", alpha=0.25, markerSize=2,color="blue")    
  plt.plot(afterAngles, alpha=0.25, label= "afterLines",color="purple")
  plt.plot(maxAfterAngles, alpha=0.7, label= "maxafter",color="red") 
  plt.plot(minAfterAngles, alpha=0.7, label= "minafter",color="red") 
  plt.plot(beforeAngles, alpha=0.7, label="before",color="black")
  plt.ylim(ymin = 0)
  _,ymax = plt.ylim()
  plt.ylim(ymax = ymax + 10)
  plt.legend(loc='upper left')  
  plt.show()


individuals = 1000
e = 0.5
k = printKValues(e,individuals)
print(k)
compareAllAngles(individuals,1000,k, 0.9, e)

