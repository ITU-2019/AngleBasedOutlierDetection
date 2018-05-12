import re
import numpy as np
import argparse

from os import listdir
from os.path import isfile, join

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def get_average(filename, dims):
    algos = ["_aABOD", "_kNN", "lbWeighted_ABOD", "_LOF", "_ABOD"]
    for algo in algos:
      sum = 0.0
      sum8 = 0.0
      sum32 = 0.0

      for i in range(51, 100):
        open_file1=open("results-org/run" + str(i) + "/" + filename + "/"+algo+"--"+dims+"--time.txt","r")
        open_file2=open("results-dimReduc/run" + str(i) + "/" + filename + "/"+algo+"--8--time.txt","r")
        open_file3=open("results-dimReduc/run" + str(i) + "/" + filename + "/"+algo+"--32--time.txt","r")

        file_lines1=open_file1.readlines()
        file_lines2=open_file2.readlines()
        file_lines3=open_file3.readlines()

        sum += float(file_lines1[1].strip())
        sum8 += float(file_lines2[1].strip())
        sum32 += float(file_lines3[1].strip())

      avg1 = sum/50.0
      avg2 = sum8/50.0
      avg3 = sum32/50.0

      up1 = "{0:.2f}".format(avg1/avg2)
      up2 = "{0:.2f}".format(avg1/avg3)
      avg = "{0:.2f}".format(avg1)
      print("file: " + filename + "\t | "+algo +" \t\t - " + avg + "s\t : +"+up1+"x \t: +" + up2 + "x")

    algos = ["BRUTE", "MEDIUM", "FAST", "TOFAST"]
    for algo in algos:

      sum = 0.0
      sum8 = 0.0
      sum32 = 0.0

      for i in range(51, 100):
        open_file1=open("results-org/run" + str(i) + "/" + filename + "/_aANGLE--"+dims+"--"+algo+"--time.txt","r")
        open_file2=open("results-dimReduc/run" + str(i) + "/" + filename + "/_aANGLE--8--"+algo+"--time.txt","r")
        open_file3=open("results-dimReduc/run" + str(i) + "/" + filename + "/_aANGLE--32--"+algo+"--time.txt","r")

        file_lines1=open_file1.readlines()
        file_lines2=open_file2.readlines()
        file_lines3=open_file3.readlines()

        sum += float(file_lines1[1].strip())
        sum8 += float(file_lines2[1].strip())
        sum32 += float(file_lines3[1].strip())

      avg1 = sum/50.0
      avg2 = sum8/50.0
      avg3 = sum32/50.0

      up1 = "{0:.2f}".format(avg1/avg2)
      up2 = "{0:.2f}".format(avg1/avg3)
      avg = "{0:.2f}".format(avg1)
      print("file: " + filename + "\t | _aANGLE--"+algo +" \t\t - " + avg + "s\t : +"+up1+"x \t: +" + up2 + "x")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    print("")
    get_average("isolet_CDE_Y", "617")
    print("")
    get_average("optdigits_39_0", "64")
    print("")
    get_average("mfeat_69_0", "649")
    print("")
