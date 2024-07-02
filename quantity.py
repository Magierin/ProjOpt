import connection as con
import csv_to_matrix as ctm

"""Returns matrix containing every taken route with their quantity (how often they appear)"""


def get_routes_quantity():
    route, route_freq, k = [el[:-3] for el in ctm.csv_to_matrix('route-all.csv')], [], 0

    for i in range(len(route)):
        m = 0
        for j in range(len(route)):
            if route[i] == route[j]:
                k += 1
                m += 1
        if [route[i], m] not in route_freq:
            route_freq.append([route[i], m])
            # if len(route[i]) == 43:
            #    print(route[i])

    lst = []
    for i in range(len(route_freq)):
        lst.append(route_freq[i][1])
        if route_freq[i][1] == 510:
            print(route_freq[i][0])

    return route_freq, lst


"""Same as getRoutesQuantity, just with a list as an input; later used for routes per hour"""


def get_routes_quantity_shadow(lst):
    route, route_freq, k = lst, [], 0

    for i in range(len(route)):
        m = 0
        for j in range(len(route)):
            if route[i] == route[j]:
                k += 1
                m += 1
        if [route[i], m] not in route_freq:
            route_freq.append([route[i], m])
            # if len(route[i]) == 43:
            #    print(route[i])

    lst1 = []
    for i in range(len(route_freq)):
        lst1.append(route_freq[i][1])
        # if route_freq[i][1] == 510:
        #    print(route_freq[i][0])

    return route_freq, lst1


"""Returns matrix containing all routes used in a particular hour: list_00 list with all routes used between
0 and 1 am"""


def get_routes_quantity_per_hour():
    route = [el for el in ctm.csv_to_matrix('route-all.csv')]
    list_00, list_01, list_02, list_03, list_04, list_05, list_06, list_07, list_08, list_09, list_10, list_11, \
        list_12, list_13, list_14, list_15, list_16, list_17, list_18, list_19, list_20, list_21, list_22, \
        list_23 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    for r in route:
        if r[-1].startswith("00"):
            list_00.append(r[:-3])
        elif r[-1].startswith("01"):
            list_01.append(r[:-3])
        elif r[-1].startswith("02"):
            list_02.append(r[:-3])
        elif r[-1].startswith("03"):
            list_03.append(r[:-3])
        elif r[-1].startswith("04"):
            list_04.append(r[:-3])
        elif r[-1].startswith("05"):
            list_05.append(r[:-3])
        elif r[-1].startswith("06"):
            list_06.append(r[:-3])
        elif r[-1].startswith("07"):
            list_07.append(r[:-3])
        elif r[-1].startswith("08"):
            list_08.append(r[:-3])
        elif r[-1].startswith("09"):
            list_09.append(r[:-3])
        elif r[-1].startswith("10"):
            list_10.append(r[:-3])
        elif r[-1].startswith("11"):
            list_11.append(r[:-3])
        elif r[-1].startswith("12"):
            list_12.append(r[:-3])
        elif r[-1].startswith("13"):
            list_13.append(r[:-3])
        elif r[-1].startswith("14"):
            list_14.append(r[:-3])
        elif r[-1].startswith("15"):
            list_15.append(r[:-3])
        elif r[-1].startswith("16"):
            list_16.append(r[:-3])
        elif r[-1].startswith("17"):
            list_17.append(r[:-3])
        elif r[-1].startswith("18"):
            list_18.append(r[:-3])
        elif r[-1].startswith("19"):
            list_19.append(r[:-3])
        elif r[-1].startswith("20"):
            list_20.append(r[:-3])
        elif r[-1].startswith("21"):
            list_21.append(r[:-3])
        elif r[-1].startswith("22"):
            list_22.append(r[:-3])
        elif r[-1].startswith("23"):
            list_23.append(r[:-3])

    """if you use this return, you have to comment the other out. This one returns every route used in this particular
    hour and additionally how often it is used"""
    """return [get_routes_quantity_shadow(list_00), get_routes_quantity_shadow(list_01),
            get_routes_quantity_shadow(list_02), get_routes_quantity_shadow(list_03),
            get_routes_quantity_shadow(list_04), get_routes_quantity_shadow(list_05),
            get_routes_quantity_shadow(list_06), get_routes_quantity_shadow(list_07),
            get_routes_quantity_shadow(list_08), get_routes_quantity_shadow(list_09),
            get_routes_quantity_shadow(list_10), get_routes_quantity_shadow(list_11),
            get_routes_quantity_shadow(list_12), get_routes_quantity_shadow(list_13),
            get_routes_quantity_shadow(list_14), get_routes_quantity_shadow(list_15),
            get_routes_quantity_shadow(list_16), get_routes_quantity_shadow(list_17),
            get_routes_quantity_shadow(list_18), get_routes_quantity_shadow(list_19),
            get_routes_quantity_shadow(list_20), get_routes_quantity_shadow(list_21),
            get_routes_quantity_shadow(list_22), get_routes_quantity_shadow(list_23)]"""

    return [list_00, list_01, list_02, list_03, list_04, list_05, list_06, list_07, list_08, list_09, list_10, list_11,
        list_12, list_13, list_14, list_15, list_16, list_17, list_18, list_19, list_20, list_21, list_22,
        list_23]


"""Returns list with dictionary elements: [{edge number/e.g. 894: quantity/e.g. 77, 'percentage': e.g. 1.024}, ...]; 
quantity is how often the edge appears in 3212 routes"""


def get_edges_quantity():
    routes = [el[:-3] for el in ctm.csv_to_matrix('route-all.csv')]
    edges = []
    counter = []
    most_used = []

    for i in range(len(routes)):
        for j in range(1, len(routes[i])):
            dic = con.get_connection(routes[i][j-1], routes[i][j])
            num = dic.get('number')
            edges.append(int(num))

    for i in range(1308):
        c = edges.count(i)
        per = c/3212 + 1
        counter.append({i: c, 'percentage': round(per, 4)})
        # percentage format: int("{:.01%}".format(per))
        if c >= 400:
            most_used.append(i)

    return most_used


"""Returns list with percentage of edge appearance in decimal"""


def get_edge_quan_per():
    per = []
    edges = get_edges_quantity()

    for edge in edges:
        per.append(edge.get('percentage'))

    return per


def get_nodes_quantity():
    routes = [el[:-3] for el in ctm.csv_to_matrix('route-all.csv')]
    nodes = []
    counter = []
    most_used = []

    for i in range(len(routes)):
        for j in range(len(routes[i])):
            nodes.append(int(routes[i][j]))

    for i in range(538):
        c = nodes.count(i)
        counter.append({i: c})
        if c >= 400:
            most_used.append(i)

    return counter, most_used


print(get_nodes_quantity())