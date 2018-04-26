import numpy as np
import matplotlib.pyplot as plt
import argparse

from fjlt import *

def parse(filename):

  with open(filename) as f:
    content = f.readlines()
  # Points.
  allPoints = []
  # Iterate over lines.
  for line in content:
    line = line.strip() # Strip whitespace
    arr = line.replace("  ", " ").split(' ')
    arr = [float(i) for i in arr]
    allPoints.append(arr)
  return allPoints

def arrayToNumpy(arr):
  a = None
  for point in arr:
    if a is None:
        a = np.array([point])
    else:
        a = np.concatenate((a, [point]))
  return a

def createDimReducedFiles(input, output):
  allPoints = parse(input)
  npPoints = arrayToNumpy(allPoints)

  q = 0.5
  for i in range(1,11):
    dims = 2**i
    res = fjlt(npPoints.transpose(),dims, q).transpose()
    np.savetxt((output) + str(dims) +".txt", res, fmt="%e")


if __name__ == "__main__":
  ap = argparse.ArgumentParser()

  ap.add_argument("-i", "--input", required=True, help= "Input file")
  ap.add_argument("-o", "--output",  required=True, help="Output file")
  
  args = vars(ap.parse_args())
  file_name = args["input"]
  output_name = args["output"]
  
  createDimReducedFiles(file_name, output_name)
  
  print("Done: " + output_name)
