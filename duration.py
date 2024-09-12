import connection as con
import csv_to_matrix as ctm
import distance as dis
import int_route_edges as ire
import parse_csv as pc

"""Returns list with the duration of every single route from route-all.csv"""


def get_routes_duration():
    data = ctm.data_all_final_new
    ls = ire.int_route_edges()
    res = []
    for i in range(len(ls)):
        summe = 0
        for j in range(len(ls[i]) - 4):
            dic = con.get_connection(str(ls[i][j]), str(ls[i][j + 1]))
            num = dic.get("number")
            name = dic.get("name")
            dist = dis.get_edge_num_dist(int(num))
            speed = float(data[i+1][data[0].index(str(name))])
            if speed == 0:
                continue
            time = (dist / speed) * 60
            summe += time
        t = float(round((round(summe, 2) - int(round(summe, 2)))*60))/100 + int(round(summe, 2))
        res.append(t)
    return res


"""To get a different timestamp for the dijkstra, change the number from data[1] to data[8] or something different;
returns list with duration of each edge in timestamp 1"""


def get_edges_duration():
    data = ctm.data_all_final_new
    dist = dis.get_distance_list()
    res = []
    for j in range(len(data[1]) - 4):
        speed = float(data[1][j])
        if speed == 0:
            continue
        time = (dist[j] / speed) * 60
        t = float(round((round(time, 2) - int(round(time, 2))) * 60)) / 100 + int(round(time, 2))
        res.append(t)
    return res


'''Returns durations for predicted speeds from csv-file predictions_2024'''


def get_edges_predicted_duration():
    data = ctm.csv_to_matrix('predictions_2024.csv')
    del data[0]
    for i in range(len(data)):
        del data[i][0:5]
    dist = dis.get_distance_list()
    res = []
    for j in range(len(data[500])-2):
        speed = float(data[500][j])
        if speed == 0:
            continue
        time = (dist[j] / speed) * 60
        t = float(round((round(time, 2) - int(round(time, 2))) * 60)) / 100 + int(round(time, 2))
        res.append(t)
    return res


'''Takes timestamp in form of '28 Mar 00_09_47'; returns list with predicted edge durations'''


def get_edges_predicted_duration_new(timestamp):
    data = ctm.data_all_final_new
    p = pc.graph

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
        if speed == 0:
            speed = 10000
        time = (dist[j-1] / speed) * 60
        t = float(round((round(time, 2) - int(round(time, 2))) * 60)) / 100 + int(round(time, 2))
        res.append(t)

    return res


'''Takes timestamp in form of '28 Mar 00_09_47'; returns list with edge durations'''


def get_duration(timestamp):
    data = ctm.csv_to_matrix('duration_prediction_new.csv')

    a = timestamp.split('.', 2)
    a[0], a[1] = a[1], a[0]
    a[2] = a[2].strip()

    for i in range(1, len(data)):
        if data[i][1:4] == a:
            return data[i][5:]
