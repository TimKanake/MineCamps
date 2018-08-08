import csv
from os.path import isfile, join
from os import listdir
import fnmatch
import numpy as np


# Returns first row of the csv file
def get_csv_row_from_file(file_path):
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            return row


def get_labels(file_path='./fer2013.csv'):
    labels = []
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            labels.append(int(row['emotion']))
    return labels


def get_training_data():
    file_names = retrieve_all_csvs_in_directory()
    file_names.sort(key=lambda f: int(filter(str.isdigit, f)))
    training_data = []
    for file_name in file_names:
        row = np.array([int(pixel) for pixel in
                        get_csv_row_from_file(file_name)['pixels'].split(' ')])
        training_data.append(row)

    return training_data


def retrieve_all_csvs_in_directory(dir_path='./resized/'):
    file_names = [[(dir_path + f) for f in listdir(dir_path) if
                  (isfile(join(dir_path, f)) and fnmatch.fnmatch(
                      join(dir_path, f), '*.csv'))]]
    return file_names


def main():
    X = get_training_data()
    Y = get_labels()

    # clf = svm.SVC()
