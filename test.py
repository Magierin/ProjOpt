import parse_csv as pc
import csv_to_matrix as ctm
import distance as dis

date = '28 Mr 00_09_46'


def get_edges_predicted_duration_new(timestamp):
    data = ctm.csv_to_matrix('data-all-final-new.csv')
    p = pc.parse_csv()

    a = timestamp.split()
    b = []

    for i in range(1, len(data)):
        if data[i][len(data[i])-3:] == a:
            b = data[i][:len(data)-4]
            break

    dist = dis.get_distance_list()
    res = []

    for j in range(1, len(p)):
        c = p[j].get('name')
        speed = float(b[data[0].index(c)])
        time = (dist[j-1] / speed) * 60
        t = float(round((round(time, 2) - int(round(time, 2))) * 60)) / 100 + int(round(time, 2))
        res.append(t)

    return res


def get_duration(timestamp):
    data = ctm.csv_to_matrix('duration_prediction_new.csv')

    a = timestamp.split('.', 2)
    a[0], a[1] = a[1], a[0]
    a[2] = a[2].strip()

    for i in range(1, len(data)):
        if data[i][1:4] == a:
            return data[i][5:]


print(get_edges_predicted_duration_new(date))
