#!/bin/bash

cd "results"
# Make 10 runs.
for i in {1..10..1}
do
    mkdir "run$i"
    cd "run$i"

    mkdir "optdigit"
    mkdir "mfeat"
    mkdir "isolet"

    # Make 10,20,30...100 dimensions.
    for j in {10..100..10}
    do

        # Test on the different data files.
        cd "optdigit"

        # idea for generating test files
        #        file,  input file,                   dims, output file
        # python gen.py ../../data/optdigits_39_0.txt $j    ../../data/optdigits_39_0--$j.txt

        ../../Outlier--KDD08.exe "../../data/optdigits_39_0--$j.txt" 1144 $j
        ../../Outlier--KDD12.exe "../../data/optdigits_39_0--$j.txt" 1144 $j
        ../../Outlier--KDDABOD.exe "../../data/optdigits_39_0--$j.txt" 1144 $j
        cd ".."

        cd "mfeat"
        ../../Outlier--KDD08.exe "../../data/mfeat_69_0--$j.txt" 410 $j
        ../../Outlier--KDD12.exe "../../data/mfeat_69_0--$j.txt" 410 $j
        ../../Outlier--ABOD.exe "../../data/mfeat_69_0--$j.txt" 410 $j
        cd ".."

        cd "isolet"
        ../../Outlier--KDD08.exe "../../data/isolet_CDE_Y--$j.txt" 910 $j
        ../../Outlier--KDD12.exe "../../data/isolet_CDE_Y--$j.txt" 910 $j
        ../../Outlier--ABOD.exe "../../data/isolet_CDE_Y--$j.txt" 910 $j
        cd ".."
    done
    cd ".."
done
