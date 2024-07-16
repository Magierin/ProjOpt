import parse_csv as pc
import csv_to_matrix as ctm
import distance as dis


def get_edges_predicted_duration_new(date):
    data = ctm.csv_to_matrix('predictions_2024_new.csv')
    p = pc.parse_csv()

    for i in range(len(data)):
        del data[i][0:4]

    dist = dis.get_distance_list()
    res = []

    for j in range(1, len(p)):
        a = p[j].get('name')
        speed = float(data[date+1][data[0].index(a)])
        time = (dist[j-1] / speed) * 60
        t = float(round((round(time, 2) - int(round(time, 2))) * 60)) / 100 + int(round(time, 2))
        res.append(t)

    return res


def create_duration_predicted_csv():
    ls = ctm.csv_to_matrix('predictions_2024_new.csv')

    csv = open('duration_prediction_new.csv', 'w')

    for i in range(len(ls)):
        if i == 0:
            ls1 = ['Year', 'Month', 'Day', 'Hour'] + [str(x) for x in range(1308)]
        else:
            ls1 = ls[i][0:4] + get_edges_predicted_duration_new(i)
        print(ls1)
        csv.writelines(','.join([str(x) for x in ls1]) + "\n")

    csv.close()


