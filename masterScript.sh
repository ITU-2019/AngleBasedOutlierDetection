#!/bin/bash

cd "results"

mkdir "run$1"
cd "run$1"

mkdir "$2"
cd "$2"
for j in 2 4 8 16 32 64 128 256 512 1024
do
    ../../Outlier-ABOD.exe       "../../data_reduced/$2-$1-$j.txt" $3 $j &&
    ../../Outlier-AproxABOD.exe  "../../data_reduced/$2-$1-$j.txt" $3 $j &&
    ../../Outlier-LBABOD.exe     "../../data_reduced/$2-$1-$j.txt" $3 $j &&
    ../../Outlier-LOF.exe        "../../data_reduced/$2-$1-$j.txt" $3 $j &&
    ../../Outlier-KNN.exe        "../../data_reduced/$2-$1-$j.txt" $3 $j &&
    ../../Outlier-AMS.exe        "../../data_reduced/$2-$1-$j.txt" $3 $j &&  
done
cd ".."

