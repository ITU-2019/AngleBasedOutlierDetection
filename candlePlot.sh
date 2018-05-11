#!/bin/bash


for file in mfeat_69_0 optdigits_39_0 isolet_CDE_Y
do
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _aABOD           -s plots/$file-approx-ABOD-plot   -n "approx ABOD $file"     &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _ABOD            -s plots/$file-Weighted-ABOD-plot -n "Weighted ABOD $file"    &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _ANGLE           -s plots/$file-Unweight-ABOD-plot -n "Unweight ABOD $file"   &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _kNN             -s plots/$file-KNN-plot           -n "KNN $file"             &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _lbWeighted_ABOD -s plots/$file-LB-ABOD-plot       -n "LB ABOD $file"         &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _LOF             -s plots/$file-LOF-plot           -n "LOF $file"             &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _aANGLE_BRUTE    -s plots/$file-VOA-BRUTE          -n "VOA BRUTE $file"       &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _aANGLE_FAST     -s plots/$file-VOA-FAST           -n "VOA FAST $file"        &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _aANGLE_MEDIUM   -s plots/$file-VOA-MEDIUM         -n "VOA MEDIUM $file"      &
    python3 build/candleGraph.py -f $file -d "results/results-dimReduc/" -a _aANGLE_TOFAST   -s plots/$file-VOA-TOFAST         -n "VOA TOFAST $file"      &
done
