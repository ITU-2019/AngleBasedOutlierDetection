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
  print(" \t e : " + str(e) + " \t n :" + str(n) )
  print(" \t k1 : " + str(k1))
  print(" \t k2 : " + str(k2))
  print(" \t k3 : " + str(k3))
  print(" \t k4 : " + str(k4))
  return floor(k4) + 1

def printE(elements,dims,reduceddims, q, e):
  maxE = 0
  minE = 1
  sumE = 0
  vals = []
  beforeDists = []
  afterDists = []
  maxAfterDists = []
  minAfterDists = []

  mu = 584
  sigma = 14.2


  a =  np.random.normal(mu,sigma,(elements,dims))
  res = fjlt(a.transpose(),reduceddims, q).transpose()
  #res = fjlt_usp(a.transpose(),reduceddims).transpose()
  for i in range(0, elements -1 ):
    j = i + 1
    beforeDistance = np.linalg.norm(a[i]-a[j])
    beforeDists.append(beforeDistance)
    maxAfterDists.append(sqrt((beforeDistance**2)*(1+e)))
    minAfterDists.append(sqrt((beforeDistance**2)*(1-e)))
    afterDistance =  np.linalg.norm(res[i]-res[j])
    afterDists.append(afterDistance)
    val = (beforeDistance - afterDistance) / beforeDistance
    vals.append(val)
    sumE += val
    if(val < minE):
      minE = val
    if(val > maxE):
      maxE = val

  afterDists =    [x for _,x in sorted(zip(beforeDists,afterDists))]
  maxAfterDists = [x for _,x in sorted(zip(beforeDists,maxAfterDists))]
  minAfterDists = [x for _,x in sorted(zip(beforeDists,minAfterDists))]
  beforeDists = sorted(beforeDists)
  
  plt.plot(afterDists,"bo", alpha=0.25, markerSize=2, label= "afterPoints")    
  plt.plot(afterDists, alpha=0.25, label= "afterLines")
  plt.plot(maxAfterDists, alpha=0.7, label= "maxafter") 
  plt.plot(minAfterDists, alpha=0.7, label= "minafter") 
  plt.plot(beforeDists, alpha=0.7, label="before")
  plt.legend(loc='upper right')  
  plt.show()

individuals = 10000
e = 0.7
k = printKValues(e,individuals)
printE(individuals,10,k, 0.9, e)

