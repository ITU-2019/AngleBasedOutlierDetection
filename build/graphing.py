import matplotlib
import matplotlib.pyplot as plt
import re
from os import listdir
from os.path import isfile, join

def directory_to_pairs(full_dir_path, regex_filter=None):
    files = [f for f in listdir(full_dir_path) if isfile(join(full_dir_path,f))]
    if regex_filter:
        regex = re.compile(regex_filter)
        files = [f for f in files if re.match(regex_filter,f)]
    datasets = []
    for filename in files:
        datasets.append((filename, file_to_pairs(full_dir_path,filename)))
    return datasets


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


def lowest_outlier(pair_list):
    lowest_pos = 0
    lowest_outlier = None
    count = 0
    for pair in pair_list:
        count += 1
        if pair[0] <= 10:
            lowest_pos = count
            lowest_outlier = pair[0]

    return (lowest_pos, lowest_outlier)


def average_outlier(pair_list):
    sum = 0
    count = 0
    for pair in pair_list:
        count += 1
        if pair[0] <= 10:
            sum += count

    return sum/10


def median_outlier(pair_list):
    lowest_pos = 0
    lowest_outlier = None
    count = 0
    outlier_count = 0
    for pair in pair_list:
        count += 1
        if pair[0] <= 10:
            outlier_count += 1
            lowest_pos = count
            lowest_outlier = pair[0]
        if outlier_count >= 5:
            return (lowest_pos, lowest_outlier)

    return (lowest_pos, lowest_outlier)


def simple_plot(datasets):
    fig, ax = plt.subplots()
    count = 10
    plt.yscale('log')
    plt.xlabel('Dimensions')
    plt.ylabel('Elements before encounter')
    plt.xticks(rotation=90)
    for filename, pair_list in datasets:
        ax.plot(filename,lowest_outlier(pair_list)[0],'rx')
        ax.plot(filename,average_outlier(pair_list),'bx')
        ax.plot(filename,median_outlier(pair_list)[0],'gx')
        count += 10

    plt.show()


def plot_originals():
    datasets = ["_aABOD-64.txt","_aABOD-617.txt","_aABOD-649.txt"]
    fig, ax = plt.subplots()
    count = 1
    for dataset in datasets:
        ax.plot(dataset,lowest_outlier(file_to_pairs(dataset,reduced=False))[0],'rx')
        count += 1
    plt.show()


data = directory_to_pairs("C:/Users/marku/OneDrive/Dokumenter/ITU/AlgDes/optdigits/optdigits/",regex_filter=r'.*aABOD.*')

simple_plot(data)
data = directory_to_pairs("C:/Users/marku/OneDrive/Dokumenter/ITU/AlgDes/optdigits/optdigits/")
simple_plot(data)
#simple_plot("_LOF-")
#plot_originals()
