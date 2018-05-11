import matplotlib
import matplotlib.pyplot as plt
import re
import numpy as np
import argparse

from os import listdir
from os.path import isfile, join

plt.style.use('ggplot')

filters = [ 
            "_kNN"            ,
            "_LOF"            ,
            "_aABOD"          ,
            "_lbWeighted_ABOD",
            "_ABOD"           ,
            "_ANGLE"          ,
            "_aANGLE_BRUTE"   ,
            "_aANGLE_MEDIUM"  ,
            "_aANGLE_FAST"    ,
            "_aANGLE_TOFAST"   ]

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def directory_to_pairs(dir_path, dataset_dir_name, runNumber, dimReducedTo):



    combinedDatasets = []
    for j in range(0,len(filters)):
        datasets = []
        for i in range (1,runNumber +1):
            full_dir_path = dir_path + "run" + str(i) + "/" + dataset_dir_name
            files = [f for f in listdir(full_dir_path) if isfile(join(full_dir_path,f))]
            regex = ('('+ filters[j] + ')(--' + str(dimReducedTo) +'.txt)')
            files = [f for f in files if re.match(regex,f)]
            

            for filename in files:
                indexes = file_to_pairs(full_dir_path,filename)
                #print(indexes)
                datasets.extend( indexes)

            #datasets.sort(key=lambda i : natural_keys(i[0]))
        
        combinedDatasets.append(datasets)
    #print(combinedDatasets)
    return combinedDatasets

def file_to_pairs(full_dir_path, filename):
    data = open(full_dir_path+filename)
    Indexlist = []
    count = 0
    for line in data.readlines():
        count += 1
        pair = line.split()
        try:
            val = int(pair[0])
            if val <= 10:
                Indexlist.append(count)
        except:
            print("Whoops")
            print(pair)
    return Indexlist


def dict_to_sorted_list(dict):
    res = []
    print(sorted(dict.keys()))
    for key in sorted(dict.keys()):
        res.append(dict[key])
    return res


def simple_plot(datasets, title, safeLocation):
    (fig , ax) = plt.subplots()

    '''outlier_dict = {}
    for run in datasets:
        for filename, pair_list in run:
            if(natural_keys(filename)[1] not in outlier_dict):
                outlier_dict[filename] = outlier_index_list(pair_list)
            else:
                outlier_dict[filename] = outlier_dict[filename]+ outlier_index_list(pair_list)
    '''
    ax.boxplot(datasets, 0,'')


    #plt.xlabel('Dimensions', labelpad=0 )
    plt.ylabel('Index', labelpad=-2 )
    plt.title(title)
    #plt.ylim((0,100))
    fig.subplots_adjust(bottom=0.4)


    plt.xticks(np.arange(12),('',
            "KNN"  ,
            "LOF"            ,
            "Approx ABOD"          ,
            "LB ABOD",
            "Weighted ABOD"           ,
            "Unweigted ABOD"          ,
            "VOA Brute"   ,
            "VOA Medium"  ,
            "VOA Fast"    ,
            "VOA Too Fast"  , 
            ''),rotation=90) #rotation_mode="anchor", y=-0.08)
    plt.savefig(safeLocation +'.png')
    #plt.show()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--file", required=True, help ="The file name the plot should be mad on")
    ap.add_argument("-d", "--directory", required=True, help="The directory containing the runs")
    #ap.add_argument("-a", "--algorithms", required=True, help="The algorithm to plot")
    ap.add_argument("-n", "--namePlot", required=True, help="The name of the plot")
    ap.add_argument("-s", "--safePlotLocation", required=True, help="Save the plot to this location")
    ap.add_argument("-r", "--runNumber",required=False, default=5, help="The number of runs to plot data from", type=int)
    ap.add_argument("-k", "--reducedToDims", required=True, default= 8, help="The number of dimensions reduced to", type=int)

    args = vars(ap.parse_args())
    file_args = args["file"]
    directory_args = args["directory"]
    #algorithm_args = args["algorithm"]

    #data = directory_to_pairs("../Results/results-with-brute/", "mfeat_69_0/" ,regex_filter=r'_aABOD--\d*.txt')
    data = directory_to_pairs(directory_args, file_args + "/", args["runNumber"], args["reducedToDims"])
    
    simple_plot(data, args["namePlot"] , args["safePlotLocation"])

