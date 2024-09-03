import csv_to_matrix as ctm

"""Returns matrix containing route-all.csv with nodes as integers, last three list elements
(timestamp) are still strings ->[[94, ..., 162, '28', 'Mr', '00_09_46'], ...]"""


def int_route_edges():
    ls = ctm.csv_to_matrix('route-all-missing-last-day.csv')
    for i in range(len(ls)):
        for j in range(len(ls[i]) - 3):
            ls[i][j] = int(ls[i][j])
    return ls
