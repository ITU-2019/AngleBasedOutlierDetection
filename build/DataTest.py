import numpy as np
import matplotlib.pyplot as plt
from fjlt import *

def parse(filename, outlierCount):
  count = 0;
  with open(filename) as f:
    content = f.readlines()

  # Points.
  allPoints = []
  outliers = []

  # Iterate over lines.
  for line in content:
    line = line.strip() # Strip whitespace
    arr = line.replace("  ", " ").split(' ')
    arr = [float(i) for i in arr]
    allPoints.append(arr)
    if count < outlierCount: # First x points are the outliers
      outliers.append(arr)
      count += 1

  return (allPoints, outliers)

def arrayToNumpy(arr):
  a = None
  for point in arr:
    if a is None:
        a = np.array([point])
    else:
        a = np.concatenate((a, [point]))
  return a

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
  return np.dot(norm1,norm2)

def plotDistances(title, a, reduceddims, outlierCount = None):
  print(
    title, ": DISTANCE: ", len(a), " elements, with ", len(a[0]), " dimensions, reduced to "
    , reduceddims, " dimensions"
  )
  vals = []
  elements = len(a)
  res = fjlt_usp(a.transpose(),reduceddims).transpose()

  select = elements
  if outlierCount != None:
    select = outlierCount

  print(select)

  for i in range(0, select):
    for j in range(i, elements ):
      for k in range(j, elements ):
        if(i != j and i != k and j != k):
          vals.append( getAngle(a[i],a[j],a[k]) - getAngle(res[i],res[j],res[k]))
  vals = [x for x in vals if (math.isnan(x) != True)]
  vals = sorted(vals)
  plt.hist(vals,"auto")
  plt.show()

def plotNormalDistances(title, a, reduceddims, outlierCount = None):
  print(
    title, ": NORMAL DISTANCE: ", len(a), " elements, with ", len(a[0]), " dimensions, reduced to "
    , reduceddims, " dimensions"
  )
  vals = []
  mu = 0
  sigma = 0.001
  elements = len(a)
  res = fjlt_usp(a.transpose(),reduceddims).transpose()
  for i in range(0,elements ):
    for j in range(i, elements ):
      for k in range(j, elements ):
        if(i != j and i != k and j != k):
          vals.append( getRad(a[i],a[j],a[k]) - getRad(res[i],res[j],res[k]))
  vals = [x for x in vals if (math.isnan(x) != True)]
  vals = sorted(vals)
  plt.hist(vals,"auto")
  plt.show()

def averageAngle(title, a, reduceddims, outlierCount = None):
  elements = len(a)
  res = fjlt_usp(a.transpose(),reduceddims).transpose()
  avg = 0
  r = None
  if outlierCount == None:
    r = range(0,elements - 3)
  else:
    r = range(0,outlierCount)
    elements = outlierCount
  for i in r:
    avg += abs(getAngle(a[i],a[i+1],a[i+2]) - getAngle(res[i],res[i+1],res[i+2]))
  print(
    title, ": AVG angle diff : ", (avg / elements), " degrees | " , len(a), " elements, with ", len(a[0]), " dimensions, reduced to "
    , reduceddims, " dimensions"
  )
  return avg / elements

def runOptDigits():
  (allPoints, outliers) = parse("data/optdigits_39_0.txt", 10)
  npPoints = arrayToNumpy(allPoints)
  npOutlier = arrayToNumpy(outliers)
  runTests("optdigits", npPoints, npOutlier)

def runMfeat():
  (allPoints, outliers) = parse("data/mfeat_69_0.txt", 10)
  npPoints = arrayToNumpy(allPoints)
  npOutlier = arrayToNumpy(outliers)
  runTests("mfeat", npPoints, npOutlier)

def runIsolet():
  (allPoints, outliers) = parse("data/isolet_CDE_Y.txt", 10)
  npPoints = arrayToNumpy(allPoints)
  npOutlier = arrayToNumpy(outliers)
  runTests("isolet", npPoints, npOutlier)

def runTests(title, allPoints, outliers):
  plotDistances(title + ", allPoints", allPoints, 25, 10)
  plotDistances(title + ", outlier", outliers, 25)

  #plotNormalDistances(title + ", allPoints", allPoints, 25)
  plotNormalDistances(title + ", outlier", outliers, 25)

  averageAngle(title + ", allPoints", allPoints, 25)
  averageAngle(title + ", allPoints-out", allPoints, 25, 10)
  averageAngle(title + ", outlier", outliers, 25)

runOptDigits();
#runMfeat();
#runIsolet();

print("Done plot")
