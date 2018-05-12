#!/bin/bash
# takes 2 argumens, run from and to
for i in $(seq $1 $2)
do
    python3 ./build/DimensionalityReduction.py -i data_original/isolet_CDE_Y.txt   -o data_reduced/isolet_CDE_Y/isolet_CDE_Y-$i-     &
    python3 ./build/DimensionalityReduction.py -i data_original/mfeat_69_0.txt     -o data_reduced/mfeat_69_0/mfeat_69_0-$i-         &
    python3 ./build/DimensionalityReduction.py -i data_original/optdigits_39_0.txt -o data_reduced/optdigits_39_0/optdigits_39_0-$i- &
done
