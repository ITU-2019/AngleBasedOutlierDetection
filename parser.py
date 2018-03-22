fname = "data/optdigits_39_0.txt"

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
    arr = line.split('  ')
    arr = [float(i) for i in arr]
    allPoints.append(arr)
    if count < outlierCount: # First x points are the outliers
      outliers.append(arr)
      count += 1

  return (allPoints, outliers)

(allPoints, outliers) = parse(fname, 10)
print (allPoints)
print (outliers)
