
import numpy as np
import matplotlib.pyplot as plt
from fjlt import *

# angle of p1
def getAngle(p1,p2,p3):
  v1 = np.subtract(p2, p1)
  v2 = np.subtract(p3, p1)
  norm1 = v1 / np.linalg.norm(v1) # The unit vector. so we dont have to devide by distance.
  norm2 = v2 / np.linalg.norm(v2)
  return np.degrees(np.arccos(np.dot(norm1,norm2)))

def getRad(p1,p2,p3):
  v1 = np.subtract(p2, p1)
  v2 = np.subtract(p3, p1)
  norm1 = v1 / np.linalg.norm(v1) # The unit vector. so we dont have to devide by distance.
  norm2 = v2 / np.linalg.norm(v2)
  return np.degrees(np.arccos(np.dot(norm1,norm2)))



print("Straigt line")
a= np.array(
        [[1,2,3],
         [1,2,3],
         [1,2,3]])
res = fjlt_usp(a,1)
print (res)
#Return results on a straigt line.


print("90 degree angle")
a1 = np.array([0,0,0])
a2 = np.array([1,0,0])
a3 = np.array([0,1,0])
a4 = np.array([1,1,0])
a= np.array(
        [a1,a2,a3,a4])
print(a)
res = fjlt_usp(a.transpose(),2).transpose()
print(res)

print(getAngle(a[0],a[1],a[2]))
print(getAngle(res[0],res[1],res[2]))

def plotRandomDistances(elements,dims,reduceddims):
  vals = []
  a = np.random.rand(elements,dims)
  res = fjlt_usp(a.transpose(),reduceddims).transpose()
  for i in range(0,elements ):
    for j in range(i, elements ):
      for k in range(j, elements ):
        if(i != j and i != k and j != k):
          vals.append( getAngle(a[i],a[j],a[k]) - getAngle(res[i],res[j],res[k]))
  vals = [x for x in vals if (math.isnan(x) != True)]
  vals = sorted(vals)
  plt.hist(vals,"auto")
  plt.show()

plotRandomDistances(30,1000,50)
plotRandomDistances(30,1000,100)


def testRandom(elements,dims,reduceddims):

  a = np.random.rand(elements,dims)
  res = fjlt_usp(a.transpose(),reduceddims).transpose()
  avg = 0
  for i in range(0,elements - 3):
    avg += abs(getAngle(a[i],a[i+1],a[i+2]) - getAngle(res[i],res[i+1],res[i+2]))
  return avg / elements

print("random tests 10 dims 1000 elements:")
print(testRandom(1000,10,10))
print(testRandom(1000,10,9))
print(testRandom(1000,10,8))
print(testRandom(1000,10,7))
print(testRandom(1000,10,6))
print(testRandom(1000,10,5))
print(testRandom(1000,10,4))

print("random tests 100 dims 1000 elements:")
print(testRandom(1000,100,50))
print(testRandom(1000,100,40))
print(testRandom(1000,100,30))
print(testRandom(1000,100,20))
print(testRandom(1000,100,15))

print("random tests 100 dims 10000 elements:")
print(testRandom(10000,100,50))
print(testRandom(10000,100,40))
print(testRandom(10000,100,30))
print(testRandom(10000,100,20))
print(testRandom(10000,100,15))

print("random tests 1000 dims 10000 elements:")
print(testRandom(1000,1000,50))
print(testRandom(1000,1000,40))
print(testRandom(1000,1000,30))
print(testRandom(1000,1000,20))
print(testRandom(1000,1000,15))




# Dont Use
def dotWithoutNormalization(p1,p2,p3):
  v1 = np.subtract(p2, p1)
  v2 = np.subtract(p3, p1)
  return np.dot(v1,v2)

## DONT USE
def plotRandomDistancesDotValues(elements,dims,reduceddims):
  vals = []
  a = np.random.rand(elements,dims)
  res = fjlt_usp(a.transpose(),reduceddims).transpose()
  for i in range(0,elements ):
    for j in range(i, elements ):
      for k in range(j, elements ):
        if(i != j and i != k and j != k):
          vals.append( dotWithoutNormalization(a[i],a[j],a[k]) - dotWithoutNormalization(res[i],res[j],res[k]))
  vals = [x for x in vals if (math.isnan(x) != True)]
  vals = sorted(vals)
  plt.hist(vals,"auto")
  plt.show()

#plotRandomDistancesDotValues(30,1000,50)


