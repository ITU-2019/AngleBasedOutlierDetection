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

  beforeAnglesInlier  = []
  beforeAnglesFringe  = []
  beforeAnglesOutlier = []
  
  afterAnglesInlier  = []
  afterAnglesFringe  = []
  afterAnglesOutlier = []  

  randomCube = np.random.rand(elements,dims)
  inlier = np.full((1, dims),0.5)
  fringe = np.full((1, dims),1)
  outlier = np.full((1, dims),2)


  broken = 0

  a = np.append(randomCube, inlier,axis=0)
  a = np.append(a, fringe,axis=0)
  a = np.append(a, outlier,axis=0)

  res = fjlt(a.transpose(),reduceddims, q).transpose()


  for i in range(0, elements - 2):
    for j in range(i + 1, elements - 1):

      beforeAnglesInlier.append( getAngle(a[elements],a[i],a[j]))
      beforeAnglesFringe.append( getAngle(a[elements+1],a[i],a[j]))
      beforeAnglesOutlier.append(getAngle(a[elements+2],a[i],a[j]))

      afterAnglesInlier.append(  getAngle(res[elements],res[i],res[j]))
      afterAnglesFringe.append(  getAngle(res[elements+1],res[i],res[j]))
      afterAnglesOutlier.append( getAngle(res[elements+2],res[i],res[j]))


      


  
  plt.plot(afterAnglesInlier, alpha=0.5, label= "Inlier",color="purple")
  plt.plot(beforeAnglesInlier, alpha=0.5, color="black")

  plt.plot(afterAnglesFringe, alpha=0.5, label= "Fringe",color="blue")
  plt.plot(beforeAnglesFringe, alpha=0.5, color="black")

  plt.plot(afterAnglesOutlier, alpha=0.5, label= "Outlier",color="green")
  plt.plot(beforeAnglesOutlier, alpha=0.5, color="black")

  plt.ylim(ymin = 0)
  _,ymax = plt.ylim()
  plt.ylim(ymax = ymax + 10)
  plt.legend(loc='upper left')  
  plt.show()


individuals = 1000
e = 0.8
k = printKValues(e,individuals)
print(k)
compareAllAngles(individuals,1000,30, 0.9, e)

