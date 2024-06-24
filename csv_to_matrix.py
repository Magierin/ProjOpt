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


def data_all_to_matrix():
    ls = [el[:-3] for el in csv_to_matrix('data-all-completed-final.csv')]
    new_ls = []
    for i in range(len(ls)):
        new_ls.append([float(el) for el in ls[i]])
    return new_ls

