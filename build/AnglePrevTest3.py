from math import log, floor, sqrt
import numpy as np
import matplotlib.pyplot as plt
from fjlt import *
from Trigonomity import *

plt.style.use('ggplot')


def printKValues(e,n):
  k1 = (log(n) * 4) / (((e**2)/2)-((e**3)/3)) # Simple proofOur paper. 
  return floor(k1) + 1


def compareAllAngles(elements,dims,reduceddims, q, e):

  beforeAngles = []
  afterAngles = []


  randomCube = np.random.rand(elements,dims)

  broken = 0

  a = randomCube
  res = fjlt(a.transpose(),reduceddims, q).transpose()

  varianceMatrixBefore = np.empty([elements])
  varianceMatrixAfter = np.empty([elements])

  for i in range(0, elements):
    for j in range(0, elements):
      for k in range(0, elements):
        if(i != j and i != k and j != k):
          beforeAngle = getAngle(a[i],a[j],a[k])
          afterAngle  = getAngle(res[i],res[j],res[k])

          beforeAngles.append(beforeAngle)
          afterAngles.append(afterAngle)
    
    varianceMatrixAfter[i] = np.array(afterAngles).var()
    varianceMatrixBefore[i] = np.array(beforeAngles).var()
    afterAngles = []
    beforeAngles = []




  

  plt.plot(varianceMatrixAfter.tolist(),"bo", alpha=0.25, markerSize=2,color="blue" , label="after")
  plt.plot(varianceMatrixBefore.tolist(),"bo", alpha=0.25, markerSize=2,color="red", label="before")
  plt.ylim(ymin = 0)
  _,ymax = plt.ylim()
  plt.ylim(ymax = ymax + 10)
  plt.legend(loc='upper left')  
  plt.show()


individuals = 100
e = 0.5
k = printKValues(e,individuals)
k = 100
print(k)
compareAllAngles(individuals,1000,k, 0.9, e)

