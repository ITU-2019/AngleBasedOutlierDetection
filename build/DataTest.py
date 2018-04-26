import numpy as np
import matplotlib.pyplot as plt
import argparse

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


def createDimReducedFiles(input, output, outliersNumber):
  (allPoints, outliers) = parse(input, outliersNumber)
  npPoints = arrayToNumpy(allPoints)
  npOutlier = arrayToNumpy(outliers)
  runTests(npPoints, npOutlier, output)

def runTests( allPoints, outliers, outputfile):
  q = 0.5
  for i in range(10,101,10):
    res = fjlt(allPoints.transpose(),i, q).transpose()
    np.savetxt((outputfile) + str(i) +".txt", res, fmt="%e")


if __name__ == "__main__":
  ap = argparse.ArgumentParser()

  ap.add_argument("-i", "--input", required=True, help= "Input file")
  ap.add_argument("-o", "--output",  required=True, help="output file")
  ap.add_argument("-u", "--outliercount", required=False, help="Number of outliers", default=10)
  
  args = vars(ap.parse_args())
  file_name = args["input"]
  output_name = args["output"]
  outlier_count = args["outliercount"]
  
  createDimReducedFiles(file_name,output_name, outlier_count)
  


  print("Done plot")
