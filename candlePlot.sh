#!/bin/bash


for file in isolet_CDE_Y
do
    python3 build/candleGraph.py -f $file -a _aABOD           -s plots2/$file-approx-ABOD-plot   -n "approx ABOD $file"     &
    #python3 build/candleGraph.py -f $file -a _ABOD            -s plots2/$file-Weighted-ABOD-plot -n "Weighted ABOD $file"    &
    #python3 build/candleGraph.py -f $file -a _ANGLE           -s plots2/$file-Unweight-ABOD-plot -n "Unweight ABOD $file"   &
    #python3 build/candleGraph.py -f $file -a _kNN             -s plots2/$file-KNN-plot           -n "KNN $file"             &
    #python3 build/candleGraph.py -f $file -a _lbWeighted_ABOD -s plots2/$file-LB-ABOD-plot       -n "LB ABOD $file"         &
    #python3 build/candleGraph.py -f $file -a _LOF             -s plots2/$file-LOF-plot           -n "LOF $file"             &
    #python3 build/candleGraph.py -f $file -a _aANGLE_BRUTE    -s plots2/$file-VOA-BRUTE          -n "VOA BRUTE $file"       &
    #python3 build/candleGraph.py -f $file -a _aANGLE_FAST     -s plots2/$file-VOA-FAST           -n "VOA FAST $file"        &
    #python3 build/candleGraph.py -f $file -a _aANGLE_MEDIUM   -s plots2/$file-VOA-MEDIUM         -n "VOA MEDIUM $file"      &
    #python3 build/candleGraph.py -f $file -a _aANGLE_TOFAST   -s plots2/$file-VOA-TOFAST         -n "VOA TOFAST $file"      &
done
