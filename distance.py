import math
import coordinates as c

# lon1 = -87.6828811088
# lon2 = -87.6746939239
# lat1 = 42.0123782948
# lat2 = 42.0126564502


"""https://www.kompf.de/gps/distcalc.html"""
"""Returns the distance from node 1 to node 2; e.g. edge 0, 26 to 27"""


def get_distance(lon1, lon2, lat1, lat2):
    lat = (lat1 + lat2) / 2 * 0.0174533
    dx = 111.3 * math.cos(lat) * (lon1 - lon2)
    dy = 111.3 * (lat1 - lat2)
    dist_in_km = math.sqrt(dx * dx + dy * dy)
    dist_in_mi = dist_in_km * 0.62137
    return dist_in_mi


"""Returns distances from all connections (edges) in a list"""


def get_distance_list():
    lst = c.get_coordinates()
    ls = []
    for i in range(len(lst)):
        lat = (lst[i][1] + lst[i][3]) / 2 * 0.0174533
        dx = 111.3 * math.cos(lat) * (lst[i][0] - lst[i][2])
        dy = 111.3 * (lst[i][1] - lst[i][3])
        dist_in_km = math.sqrt(dx * dx + dy * dy)
        dist_in_mi = dist_in_km * 0.62137
        ls.append(dist_in_mi)
    return ls


"""Returns distance from node 1 to node 2; input is the edge number (<=> index)"""


def get_edge_num_dist(num):
    return get_distance_list()[num]


print(get_distance_list())
