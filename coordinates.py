import parse_csv as pc

"""Returns matrix containing coordinates from every edge: [[-87.6997452648, 42.0121135858, -87.6902409033,
 42.0123000867], ...]"""


def get_coordinates():
    ls = pc.parse_csv()
    co = []
    for i in range(1, len(ls)):
        lon1 = ls[i].get("lon1")
        lat1 = ls[i].get("lat1")
        lon2 = ls[i].get("lon2")
        lat2 = ls[i].get("lat2")
        co.append([float(lon1), float(lat1), float(lon2), float(lat2)])
    return co
