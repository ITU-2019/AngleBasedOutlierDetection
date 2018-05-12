#!/bin/bash

file1="optdigits_39_0"
file2="mfeat_69_0"
file3="isolet_CDE_Y"

./mas.sh 1144 64 "$file1" &
./mas.sh 910 617 "$file3" &
./mas.sh 410 649 "$file2" &
