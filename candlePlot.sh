#!/bin/bash


for file in mfeat_69_0 optdigits_39_0 isolet_CDE_Y
do
    python3 build/candleGraph.py -f $file -d "../Results/results-with-brute/" -a _aABOD -s plots/$file-approx-ABOD-plot -n "approx ABOD $file"     &
    python3 build/candleGraph.py -f $file -d "../Results/results-with-brute/" -a _ABOD -s plots/$file-ABOD-plot -n "ABOD $file"                    &
    python3 build/candleGraph.py -f $file -d "../Results/results-with-brute/" -a _ANGLE -s plots/$file-VOA-plot -n "Fast VOA $file"                &
    python3 build/candleGraph.py -f $file -d "../Results/results-with-brute/" -a _kNN -s plots/$file-KNN-plot -n "KNN $file"                       &
    python3 build/candleGraph.py -f $file -d "../Results/results-with-brute/" -a _lbWeighted_ABOD -s plots/$file-LB-ABOD-plot -n "LB ABOD $file"   &
    python3 build/candleGraph.py -f $file -d "../Results/results-with-brute/" -a _LOF -s plots/$file-LOF-plot -n "LOF $file"                       &
done
