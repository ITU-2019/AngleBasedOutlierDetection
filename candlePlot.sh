#!/bin/bash


for file in mfeat_69_0 optdigits_39_0 isolet_CDE_Y
do
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _aABOD           -s plots/dimCompare/$file-approx-ABOD-plot   -n "approx ABOD $file"            &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _ABOD            -s plots/dimCompare/$file-Weighted-ABOD-plot -n "Weighted ABOD $file"          &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _ANGLE           -s plots/dimCompare/$file-Unweight-ABOD-plot -n "Unweight ABOD $file"          &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _kNN             -s plots/dimCompare/$file-KNN-plot           -n "KNN $file"                    &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _lbWeighted_ABOD -s plots/dimCompare/$file-LB-ABOD-plot       -n "LB ABOD $file"                &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _LOF             -s plots/dimCompare/$file-LOF-plot           -n "LOF $file"                    &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _aANGLE_BRUTE    -s plots/dimCompare/$file-VOA-BRUTE          -n "VOA BRUTE $file"              &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _aANGLE_FAST     -s plots/dimCompare/$file-VOA-FAST           -n "VOA FAST $file"               &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _aANGLE_MEDIUM   -s plots/dimCompare/$file-VOA-MEDIUM         -n "VOA MEDIUM $file"             &
    python3 build/candleGraph.py -r 100 -f $file -d "results/results-dimReduc/" -a _aANGLE_TOFAST   -s plots/dimCompare/$file-VOA-TOFAST         -n "VOA TOFAST $file"             &
    python3 build/candleGraphOrgCompare.py -r 100 -f $file -d "results/results-dimReduc/" -s plots/algoCompare/$file-CompareAll-8  -n "Compare All $file 8 dim reduced"     -k 8    &
    python3 build/candleGraphOrgCompare.py -r 100 -f $file -d "results/results-dimReduc/" -s plots/algoCompare/$file-CompareAll-16 -n "Compare All $file 16 dim reduced"    -k 16   &
    python3 build/candleGraphOrgCompare.py -r 100 -f $file -d "results/results-dimReduc/" -s plots/algoCompare/$file-CompareAll-32 -n "Compare All $file 32 dim reduced"    -k 32   &
    python3 build/candleGraphOrgCompare.py -r 100 -f $file -d "results/results-dimReduc/" -s plots/algoCompare/$file-CompareAll-64 -n "Compare All $file 64 dim reduced"    -k 64   &
    python3 build/candleGraphOrgCompare.py -r 100 -f $file -d "results/results-dimReduc/" -s plots/algoCompare/$file-CompareAll-1024 -n "Compare All $file 1024 dim reduced"    -k 1024   &
    
done

python3 build/candleGraphOrgCompare.py -r 100 -f mfeat_69_0 -d "results/results-org/" -s plots/algoCompare/mfeat_69_0-CompareAll-ORG -n "Compare All mfeat_69_0 Original Data"              -k 649  &
python3 build/candleGraphOrgCompare.py -r 100 -f optdigits_39_0 -d "results/results-org/" -s plots/algoCompare/optdigits_39_0-CompareAll-ORG -n "Compare All optdigits_39_0 Original Data"  -k 64   &
python3 build/candleGraphOrgCompare.py -r 100 -f isolet_CDE_Y -d "results/results-org/" -s plots/algoCompare/isolet_CDE_Y-CompareAll-ORG -n "Compare All isolet_CDE_Y Original Dataed"      -k 617  &
