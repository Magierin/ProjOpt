import csv_to_matrix as ctm
import int_route_edges as ire
import connection as con
import distance as dis


"""Returns list with the duration of every single route from route-all.csv"""


def get_routes_duration():
    data = ctm.csv_to_matrix('data-all-final-new.csv')
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


print(get_routes_duration())


"""To get a different timestamp for the dijkstra, change the number from data[1] to data[8] or something different"""


def get_edges_duration():
    data = ctm.csv_to_matrix('data-all-final-new.csv')
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
