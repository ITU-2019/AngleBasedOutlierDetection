#!/bin/bash
# Outlier-kNN.exe "data/optdigits_39_0.txt" 1144  64 &
# Outlier-kNN.exe "data/mfeat_69_0.txt"      410 649 &
# Outlier-kNN.exe "data/isolet_CDE_Y.txt"    910 617

cd "results"

file1="optdigits_39_0"
file2="mfeat_69_0"
file3="isolet_CDE_Y"  

for j in {51..100}
do
    mkdir "run$j"
    cd "run$j"

    mkdir "$file3"
    cd "$file3"

    ../../Outlier.exe        "../../../data_original/$3.txt" $1 $2 &

    cd ".."
    cd ".."
done
cd ".."
