import parse_csv as pc
import csv_to_matrix as ctm
import distance as dis
import quantity as quan
import connection as con

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
        if speed == 0:
            speed = 0.001
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


def get_edges_quan_per_hour_per(hour):
    routes = quan.get_routes_quantity_per_hour()[hour]
    edges = []
    counter = []

    for i in range(len(routes)):
        for j in range(1, len(routes[i])):
            dic = con.get_connection(routes[i][j - 1], routes[i][j])
            num = dic.get('number')
            edges.append(int(num))

    for i in range(1308):
        c = edges.count(i)
        per = c / len(routes)
        counter.append(round(per, 4))

    return counter


def get_timestamp():
    data = ctm.csv_to_matrix('data-all-final-new.csv')
    test_data = ctm.csv_to_matrix('route-all.csv')
    stamp = []

    for i in range(1, len(test_data)+1):
        stamp.append(' '.join(data[i][len(data[i])-3:]))

    return stamp


def get_timestamp_val():
    data = ctm.csv_to_matrix('data-all-final-new.csv')
    test_data = ctm.csv_to_matrix('route-all-missing-last-day.csv')[3212:]
    stamp = []

    for i in range(1, len(test_data)+1):
        stamp.append(' '.join(data[i][len(data[i])-3:]))

    return stamp


# timestamp = '12 Mar 00_35_34'
def get_timestamp_route_list(timestamp):
    ts = timestamp.split()
    hour = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23']

    ls = []
    for i in hour:
        if ts[2].startswith(i):
            ls = quan.get_routes_quantity_per_hour()[hour.index(i)]
            break

    return ls


def get_timestamp_all():
    data = ctm.csv_to_matrix('data-all-final-new.csv')
    stamp = []

    for i in range(1, len(data)):
        stamp.append(' '.join(data[i][len(data[i])-3:]))

    return stamp


def get_speed_from_timestamp(timestamp):
    stamps = get_timestamp_all()
    speed = 0

    for i in range(len(stamps)):
        if stamps[i] == timestamp:
            speeds = ctm.csv_to_matrix('data-all-final-new.csv')[i + 1]
            for j in range(len(speeds)-3):
                speed += float(speeds[j])
            duration = speed/len(speeds)
            return duration
