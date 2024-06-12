import csv_to_matrix as ctm
import int_route_edges as ire
import connection as con
import distance as dis

"""Returns list with the duration of every single route from route-all.csv"""


def get_routes_duration():
    data = ctm.csv_to_matrix('data-all-completed-final.csv')
    ls = ire.int_route_edges()
    res = []
    for i in range(len(ls)):
        summe = 0
        for j in range(len(ls[i]) - 4):
            dic = con.get_connection(str(ls[i][j]), str(ls[i][j + 1]))
            num = dic.get("number")
            dist = dis.get_edge_num_dist(int(num))
            speed = float(data[i+1][int(num)])
            if speed == 0:
                continue
            time = (dist / speed) * 60
            summe += time
        t = float(round((round(summe, 2) - int(round(summe, 2)))*60))/100 + int(round(summe, 2))
        res.append(t)
    return res
