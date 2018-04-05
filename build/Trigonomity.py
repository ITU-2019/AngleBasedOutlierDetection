
import numpy as np

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

# using lengths of sides.
def getAngle2(a,b,c):
  if(b+c < a ):
    return 180
  if(a <= 0):
    return 0
  return np.degrees(np.arccos((b**2 + c**2 - (a**2))/(2*b*c)))


# Dont Use
def dotWithoutNormalization(p1,p2,p3):
  v1 = np.subtract(p2, p1)
  v2 = np.subtract(p3, p1)
  return np.dot(v1,v2)
