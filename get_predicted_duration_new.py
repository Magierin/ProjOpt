import csv_to_matrix as ctm
import distance as dis
import parse_csv as pc

'''Returns dictionary; key: edge name from graph_updated.csv, value: distance from node A to node B in miles'''


def distance_dict():
    data = ctm.csv_to_matrix("graph_updated.csv")
    name = []

    for i in range(1, len(data)):
        name.append(data[i][1])

    dist = dis.get_distance_list()
    names = dict(zip(name, dist))

    return names


'''Converts list elements '"94"' to '94', so we can work with the numbers'''


def convert_list_elements():
    data = ctm.csv_to_matrix('predictions_2024_last.csv')
    ls = []

    for m in range(len(data)):
        tmp = []
        for n in range(len(data[0])):
            tmp.append(data[m][n].replace('"', ''))
        ls.append(tmp)

    return ls


'''Takes number that correlates to the index of a line in data_all_final_new: number 0 -> timestamp 28 Mar 00_09_47;
returns list with predicted duration of visiting a edge (edge name)'''


def get_edges_predicted_duration_new(date):
    ls = convert_list_elements()

    pn = pc.parse_csv('grah_updated.csv')
    p = []
    for i in range(1, len(pn)):
        p.append(pn[i].get('name'))

    for i in range(len(ls)):
        del ls[i][0:4]

    dist = distance_dict()
    res = []

    for j in range(len(p)):
        if str(p[j]) in dist.keys():
            speed = float(ls[date][j])
            time = (dist.get(str(p[j])) / speed) * 60
            t = float(round((round(time, 2) - int(round(time, 2))) * 60)) / 100 + int(round(time, 2))
            res.append(t)

    return res


'''Creates csv duration_prediction_last.csv'''


def create_duration_predicted_csv():
    ls = convert_list_elements()

    p = ls[0]

    p.remove('867')
    p.remove('875')
    p.remove('876')
    p.remove('882')
    p.remove('883')
    p.remove('1026')
    p.remove('1035')
    p.remove('1061')

    csv = open('duration_prediction_last.csv', 'w')

    for i in range(len(ls)):
        if i == 0:
            ls1 = p
        else:
            ls1 = ls[i][0:4] + get_edges_predicted_duration_new(i)
        csv.writelines(','.join([str(x) for x in ls1]) + "\n")

    csv.close()
