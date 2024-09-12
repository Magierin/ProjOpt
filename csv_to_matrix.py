"""Returns matrix containing any csv file; from .csv to matrix (list in list, [[],[], ...]);
all list-elements (ls[][]) are strings -> e.g. [['94', ..., '162', '28', 'Mr', '00_09_46'], ...]"""


def csv_to_matrix(filename):
    fd = open(filename)
    ls = []
    for line in fd:
        spalten = line.split(',')
        gespalten = [x.strip() for x in spalten]
        ls.append(gespalten)
    fd.close()
    return ls


# global variables
data_all_final_new = csv_to_matrix('data-all-final-new.csv')
route_all_missing_last_day = csv_to_matrix('route-all-missing-last-day.csv')
