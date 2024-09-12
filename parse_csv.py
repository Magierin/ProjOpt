"""Method from Computerorientierte Mathematik 1 Skript 2022/23"""

"""Returns a list with dictionary elements containing information from graph.csv 
(e.g. ls[0] = {number: 0, name: 1002, from: 26, to: 27, lon1:...})"""


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


# global variable
graph = parse_csv('graph.csv')
