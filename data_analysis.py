import csv
import sys
import collections
import matplotlib.pyplot as plt
import math


def analyze_emotion(csv_file_path, emotion):
    emotion_levels = get_emotion_levels(csv_file_path, emotion)

    total_emotion_value = 0
    max_emotion_value = sys.float_info.min

    for key, value in emotion_levels.items():
        total_emotion_value += value
        if value > max_emotion_value:
            max_emotion_value = value

    average_emotion_value = float(total_emotion_value/len(emotion_levels))
    print('average emotion value: ', average_emotion_value)
    print('max emotion value: ', max_emotion_value)

    dist_from_mean_sum = 0
    for key, value in emotion_levels.items():
        dist_from_mean_sum += (value - average_emotion_value)**2
    std_deviation = math.sqrt(dist_from_mean_sum/(len(emotion_levels)-1))

    print('standard deviation: ', std_deviation)

    areas_of_interest = set()
    for key, value in emotion_levels.items():
        if value - (3 * std_deviation) > 0:
            areas_of_interest.add(int(int(key)/1000))
    areas_of_interest = sorted(areas_of_interest)
    for x in areas_of_interest:
        print(str(int(x / 60)) + ':' + str(x % 60))


def convert_delimited_txt_to_csv(txt_file_path, csv_file_path):
    in_txt = csv.reader(open(txt_file_path, "rb"), delimiter='\t')
    out_csv = csv.writer(open(csv_file_path, 'wb'))
    out_csv.writerows(in_txt)


def get_emotion_levels(file_path, emotion):
    with open(file_path) as csvfile:
        data = csv.DictReader(csvfile)
        values = {}
        vals = []
        for row in data:
            if int(row['NoOfFaces']) == 1 and \
             float(row[emotion + ' Evidence']) > 0:
                values[row['Timestamp']] = float(row[emotion + ' Evidence'])
                # vals.append(float(row[emotion + ' Evidence']))
    return values


if __name__ == '__main__':
    analyze_emotion(
        '/Users/timkanake/Desktop/imotionsdata.csv', 'Confusion')
