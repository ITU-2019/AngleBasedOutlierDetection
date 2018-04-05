from math import log, floor, sqrt
import numpy as np
import matplotlib.pyplot as plt
from fjlt import *
from Trigonomity import *


def printKValues(e,n):
  k1 = 4/((((e**2)/2)-((e**3)/3)))* log(n) # Simple proofOur paper. 
  k2 = 9/((((e**2))-(2*(e**3)/3)))* log(n) #
  k3 = (e**-2)*log(n)
  print(" \t e : " + str(e) + " \t n :" + str(n) )
  print(" \t k1 : " + str(k1))
  print(" \t k2 : " + str(k2))
  print(" \t k3 : " + str(k3))
  return floor(k3) + 1

def printE(elements,dims,reduceddims, q, e):
  maxE = 0
  minE = 1
  sumE = 0
  vals = []
  beforeDists = []
  afterDists = []
  maxAfterDists = []
  minAfterDists = []
  a = np.random.rand(elements,dims)
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
  minE = minE - sumE/len(a)
  maxE = maxE - sumE/len(a)
  vals = list(map(lambda x: x -sumE/len(a), vals))
  vals = sorted(vals)
  #plt.hist(vals,"auto")

  
  plt.hist(beforeDists,"auto", alpha=0.25, label="before")
  plt.hist(afterDists,"auto", alpha=0.25, label= "after")    
  plt.hist(maxAfterDists,"auto", alpha=0.25, label= "maxafter") 
  plt.hist(minAfterDists,"auto", alpha=0.25, label= "minafter") 
  plt.legend(loc='upper right')  
  plt.show()

e = 0.1
k = printKValues(e,1000)
printE(1000,1000,k, 0.9, e)

