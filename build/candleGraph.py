import matplotlib
import matplotlib.pyplot as plt
import re
import numpy as np
import argparse

from os import listdir
from os.path import isfile, join

plt.style.use('ggplot')

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def directory_to_pairs(dir_path, dataset_dir_name, regex_filter, runNumber):
    combinedDatasets = []
    for i in range (1,runNumber +1):
        full_dir_path = dir_path + "run" + str(i) + "/" + dataset_dir_name
        files = [f for f in listdir(full_dir_path) if isfile(join(full_dir_path,f))]

        if regex_filter:
            regex = re.compile(regex_filter)
            files = [f for f in files if re.match(regex_filter,f)]
        datasets = []

        for filename in files:
            datasets.append((filename, file_to_pairs(full_dir_path,filename)))

        datasets.sort(key=lambda i : natural_keys(i[0]))
        combinedDatasets.append(datasets)
    return combinedDatasets

def file_to_pairs(full_dir_path, filename):
    data = open(full_dir_path+filename)
    pair_list = []
    for line in data.readlines():
        pair = line.split()
        try:
            pair = (int(pair[0]),float(pair[1]))
            pair_list.append(pair)
        except:
            print("Whoops")
            print(pair)
    return pair_list



def outlier_index_list(pair_list):
    outlier_index_list_res = []
    count = 0
    for pair in pair_list:
        count += 1
        if pair[0] <= 10:
            outlier_index_list_res.append(count)
    return outlier_index_list_res

def dict_to_sorted_list(dict):
    res = []
    for key in sorted(dict.keys()):
        res.append(dict[key])
    return res


def simple_plot(datasets, title, safeLocation):
    (_ , ax) = plt.subplots()

    outlier_dict = {}
    
    for run in datasets:
        for filename, pair_list in run:
            if(natural_keys(filename)[1] not in outlier_dict):
                outlier_dict[natural_keys(filename)[1]] = outlier_index_list(pair_list)
            else:
                outlier_dict[natural_keys(filename)[1]] = outlier_dict[natural_keys(filename)[1]]+ outlier_index_list(pair_list)

    ax.boxplot(dict_to_sorted_list(outlier_dict), 0,'')


    plt.xlabel('Dimensions', labelpad=-5 )
    plt.ylabel('Index', labelpad=-2 )
    plt.title(title)
    #plt.ylim((0,100))
    plt.xticks(np.arange(12),('','2','4','8','16','32','64','128','256','512','1024', ''),rotation=20)
    plt.savefig(safeLocation +'.png')
    #plt.show()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--file", required=True, help ="The file name the plot should be mad on")
    ap.add_argument("-d", "--directory", required=True, help="The directory containing the runs")
    ap.add_argument("-a", "--algorithm", required=True, help="The algorithm to plot")
    ap.add_argument("-n", "--namePlot", required=True, help="The name of the plot")
    ap.add_argument("-s", "--safePlotLocation", required=True, help="Save the plot to this location")
    ap.add_argument("-r", "--runNumber",required=False, default=5, help="The number of runs to plot data from")

    args = vars(ap.parse_args())
    file_args = args["file"]
    directory_args = args["directory"]
    algorithm_args = args["algorithm"]

    #data = directory_to_pairs("../Results/results-with-brute/", "mfeat_69_0/" ,regex_filter=r'_aABOD--\d*.txt')
    data = directory_to_pairs(directory_args, file_args + "/" , ('('+ algorithm_args + ')((--\d+.txt)|(\d+--.txt))'), args["runNumber"])
    
    simple_plot(data, args["namePlot"] , args["safePlotLocation"])

