#!/bin/bash
# Ex: ./originalExe.sh 910 617 "isolet_CDE_Y"
cd "results"

for j in {51..100}
do
    mkdir "run$j"
    cd "run$j"

    mkdir "$3"
    cd "$3"
    ../../Outlier.exe       "../../../data_original/$3.txt" $1 $2 &
   
    cd ".."
    cd ".."
done
cd ".."
