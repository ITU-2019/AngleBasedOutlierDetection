

#!/bin/bash
# Outlier-kNN.exe "data/optdigits_39_0.txt" 1144  64 &
# Outlier-kNN.exe "data/mfeat_69_0.txt"      410 649 &
# Outlier-kNN.exe "data/isolet_CDE_Y.txt"    910 617 


for k in 1 2 3 4 5
do
    ./masterScript.sh $k optdigits_39_0  1144 &
    ./masterScript.sh $k mfeat_69_0       410 &
    ./masterScript.sh $k isolet_CDE_Y     910 &
done


