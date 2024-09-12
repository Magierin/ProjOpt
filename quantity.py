import csv_to_matrix as ctm
import connection as con

"""Returns matrix containing every taken route with their quantity (how often they appear)"""


def get_routes_quantity():
    route, route_freq, k = [el[:-3] for el in ctm.route_all_missing_last_day], [], 0

    for i in range(len(route)):
        m = 0
        for j in range(len(route)):
            if route[i] == route[j]:
                k += 1
                m += 1
        if [route[i], m] not in route_freq:
            route_freq.append([route[i], m])

    lst = []
    for i in range(len(route_freq)):
        lst.append(route_freq[i][1])

    return route_freq


"""Returns matrix containing all routes used in a particular hour: list_00 list with all routes used between0 and 1 am"""


def get_routes_quantity_per_hour():
    routes = [el for el in ctm.route_all_missing_last_day]
    list = [[] for x in range(24)]

    for route in routes:
        list[int(route[-1][0:2])].append(route[:-3])

    return list


'''Returns all historical routes in a list'''


def get_routes():
    return [el[:-3] for el in ctm.route_all_missing_last_day]


'''Takes list of routes from one particular hour; returns list with percentages, how often edges were found in 
historical routes from one particular hour'''


def get_edges_quan_per_hour_percentage(hour_routes):
    routes = hour_routes
    edges = []
    counter = []

    for i in range(len(routes)):
        for j in range(1, len(routes[i])):
            dic = con.get_connection(str(routes[i][j - 1]), str(routes[i][j]))
            num = dic.get('number')
            edges.append(int(num))

    for i in range(1308):
        c = edges.count(i)
        per = c / len(routes)
        counter.append(round(per, 4))

    return counter


"""Returns list with dictionary elements: [{edge number/e.g. 894: quantity/e.g. 77, 'percentage': e.g. 1.024}, ...]; 
quantity is how often the edge appears in 3212 routes"""


def get_edges_quantity():
    routes = [el[:-3] for el in ctm.route_all_missing_last_day]
    edges = []
    counter = []

    for i in range(len(routes)):
        for j in range(1, len(routes[i])):
            dic = con.get_connection(routes[i][j-1], routes[i][j])
            num = dic.get('number')
            edges.append(int(num))

    for i in range(1308):
        c = edges.count(i)
        per = c/len(routes)
        counter.append({i: c, 'percentage': round(per, 4)})

    return counter


"""Returns list with percentage of edge appearance in decimal"""


def get_edge_quan_per():
    per = []
    edges = get_edges_quantity()

    for edge in edges:
        per.append(edge.get('percentage'))

    return per


"""Returns list dictionaries as elements: [{0: 0}, ..., {94: 3212}, ... ] with {node: frequency in historical routes}"""


def get_nodes_quantity():
    routes = [el[:-3] for el in ctm.route_all_missing_last_day]
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

    return counter


'''Returns list eith percentages of how often nodes appear in historical routes'''


def get_nodes_quan_per():
    per = []
    nodes = get_nodes_quantity()

    for i in range(len(nodes)):
        per.append(nodes[i].get(i)/3212)

    return per
