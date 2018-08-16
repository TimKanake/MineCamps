import csv
from os.path import isfile, join
from os import listdir
import fnmatch
import numpy as np
from sklearn import svm


# Returns first row of the csv file
def get_csv_row_from_file(file_path):
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        items = []
        values = []
        for row in data:
            while row:
                items.append(row.popitem(last=False))
        for item in items:
            values.append(item[1])
        return values


def get_labels(file_path='./fer2013.csv'):
    labels = []
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            labels.append(int(row['emotion']))
    return labels


def get_training_data(dir_path):
    valid_files = []
    file_names = retrieve_all_csvs_in_directory(dir_path)
    file_names.sort(key=lambda f: int(f.split('/')[-1].split('.')[0]))
    valid_files = [int(f.split('/')[-1].split('.')[0]) for f in file_names]
    training_data = []
    for i in range(len(file_names)):
        row = get_csv_row_from_file(file_names[i])
        training_data.append(row)
    
    print(len(training_data))
    print(valid_files)

    return valid_files, training_data


def retrieve_all_csvs_in_directory(dir_path='./resized/'):
    file_names = [(dir_path + f) for f in listdir(dir_path) if
                  (isfile(join(dir_path, f)) and fnmatch.fnmatch(
                      join(dir_path, f), '*.csv'))]
    return file_names


def main():
    # get training data and train the classifier
    X = get_training_data(
        '/Users/timkanake/Documents/githubProj/OpenFace/build/bin/processed/')
    # Y = get_labels()
    # clf = svm.SVC()


if __name__ == "__main__":
    main()
