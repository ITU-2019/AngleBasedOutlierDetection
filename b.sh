#!/bin/bash
../../Outlier--ABOD.exe       "../../../data_original/$3.txt" $1 $2
../../Outlier--AproxABOD.exe  "../../../data_original/$3.txt" $1 $2
../../Outlier--LBABOD.exe     "../../../data_original/$3.txt" $1 $2
../../Outlier--LOF.exe        "../../../data_original/$3.txt" $1 $2
../../Outlier--KNN.exe        "../../../data_original/$3.txt" $1 $2
../../Outlier--AMS-Tofast.exe "../../../data_original/$3.txt" $1 $2
../../Outlier--AMS-Fast.exe   "../../../data_original/$3.txt" $1 $2
../../Outlier--AMS-Medium.exe "../../../data_original/$3.txt" $1 $2
../../Outlier--AMS-Brute.exe  "../../../data_original/$3.txt" $1 $2

