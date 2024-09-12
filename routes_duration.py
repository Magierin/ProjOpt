import math

def csv_to_matrix(file):
    fd = open(file)
    ls = []
    for line in fd:
        spalten = line.split(',')
        gespalten = [x.strip() for x in spalten]
        ls.append(gespalten)
    fd.close()
    return ls


def int_route_edges():
    ls = csv_to_matrix('route-all-missing-last-day.csv')
    for i in range(len(ls)):
        for j in range(len(ls[i]) - 3):
            ls[i][j] = int(ls[i][j])
    return ls


def parse_csv(file):
    fd = open(file)
    ls = []
    for line in fd:
        spalten = line.split(',')
        gespalten = [x.strip() for x in spalten]
        num, name, fro, to, lon1, lat1, lon2, lat2 = gespalten
        ls.append({'number': num, 'name': name, 'from': fro, 'to': to, 'lon1': lon1, 'lat1': lat1,
                   'lon2': lon2, 'lat2': lat2})
    fd.close()
    return ls


def get_connection(s, f):
    p = parse_csv('graph.csv')
    for i in range(1, len(p)):
        if ('from', s) in p[i].items() and ('to', f) in p[i].items():
            return p[i]


def get_coordinates():
    ls = parse_csv('graph.csv')
    co = []
    for i in range(1, len(ls)):
        lon1 = ls[i].get("lon1")
        lat1 = ls[i].get("lat1")
        lon2 = ls[i].get("lon2")
        lat2 = ls[i].get("lat2")
        co.append([float(lon1), float(lat1), float(lon2), float(lat2)])
    return co


def get_distance_list():
    lst = get_coordinates()
    ls = []
    for i in range(len(lst)):
        lat = (lst[i][1] + lst[i][3]) / 2 * 0.0174533
        dx = 111.3 * math.cos(lat) * (lst[i][0] - lst[i][2])
        dy = 111.3 * (lst[i][1] - lst[i][3])
        dist_in_km = math.sqrt(dx * dx + dy * dy)
        dist_in_mi = dist_in_km * 0.62137
        ls.append(dist_in_mi)
    return ls


def get_edge_num_dist(num):
    return get_distance_list()[num]


def get_routes_duration():
    data = csv_to_matrix('data_all_final_new.csv')
    ls = int_route_edges()
    res = []
    for i in range(len(ls)):
        summe = 0
        for j in range(len(ls[i]) - 4):
            dic = get_connection(str(ls[i][j]), str(ls[i][j + 1]))
            num = dic.get("number")
            name = dic.get("name")
            dist = get_edge_num_dist(int(num))
            speed = float(data[i+1][data[0].index(str(name))])
            if speed == 0:
                continue
            time = (dist / speed) * 60
            summe += time
        t = float(round((round(summe, 2) - int(round(summe, 2)))*60))/100 + int(round(summe, 2))
        res.append(t)
    return res
