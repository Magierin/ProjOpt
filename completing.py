import connection as con
import csv_to_matrix as ctm
import parse_csv as pc

"""Creates data-all-completed.csv: half completed data, edge weight from reversed edge"""


def completing():
    ls = ctm.csv_to_matrix('data-all.csv')

    for i in range(len(ls[0]) - 3):
        ls[0][i] = int(ls[0][i])

    lst1 = []
    m = 1
    for j in range(len(ls[0]) - 3):
        for n in range(j + m, 1310):
            if ls[0][j] == n:
                break
            else:
                lst1.append(n)
                m += 1
                continue

    p = pc.graph
    n = 0
    ls2 = []
    ls4 = []
    for i in lst1:
        for j in range(1, len(p)):
            if ('number', str(i)) in p[j].items():
                f = p[j]["from"]
                t = p[j]["to"]
                if con.get_connection(f, t) and con.get_connection(t, f):
                    x = con.get_connection(f, t)
                    y = con.get_connection(t, f)
                    ls2.append(int(y["number"]))
                    ls4.append(int(x["number"]))
                    n += 1
    z = list(map(list, zip(ls4, ls2)))

    ls2.sort()
    ls3 = list(set(lst1).intersection(ls2))
    ls3.sort()

    for i in ls3:
        ls2.remove(i)

    m = 0
    for i in range(len(z)):
        if z[i - m][1] in ls3:
            z.remove(z[i - m])
            m += 1

    z.remove([236, 517])
    z.remove([388, 1304])
    z.remove([437, 312])
    z.remove([517, 236])
    z.remove([838, 1090])

    x = open('data-all-completed.csv', 'w')

    ind2 = 0
    for j in range(len(z)):
        n = 0
        for row in ls:
            m = 0
            ind1 = ls[0].index(z[j][1])
            if row == ls[0]:
                for i in range(len(ls[0]) - 3):
                    if z[j][0] > ls[0][i]:
                        n = z[j][0] - ls[0][i]
                        continue
                ls = []
                ind2 = row.index(z[j][0] - n)
                m += 1
            row = row[:ind2 + 1] + [row[ind1]] + row[ind2 + 1:]
            if m == 1:
                row[ind2 + 1] = z[j][0]
            ls.append(row)

    for i in range(len(ls)):
        x.writelines(','.join([str(x) for x in ls[i]]) + "\n")

    for i in range(len(ls[0]) - 3):
        if ls[0][i] == ls[0][i + 1]:
            print(ls[0][i])

    x.close()


"""Returns matrix containing neighbors from all missing edges in data-all-completed.csv"""


def get_neighbors(missing_ind):
    neighbors = []
    p = pc.graph

    for i in missing_ind:
        tmp_list = []

        for j in range(1, len(p)):
            if ('name', str(i)) in p[j].items():
                f = p[j]['from']
                t = p[j]['to']

                for n in range(1, len(p)):
                    if ('to', f) in p[n].items():
                        x1 = int(p[n]['name'])
                        if x1 not in missing_ind:
                            tmp_list.append(x1)
                    elif ('from', t) in p[n].items():
                        y1 = int(p[n]['name'])
                        if y1 not in missing_ind:
                            tmp_list.append(y1)

        neighbors.append(tmp_list)

    return neighbors


"""Creates data-all-completed-final.csv, the final completed data set using the average neighbors speed"""


def get_speed_from_neighbors():
    ls = ctm.csv_to_matrix('data-all-completed.csv')

    for i in range(len(ls[0]) - 3):
        ls[0][i] = int(ls[0][i])

    missing_ind = [x for x in range(1, 1310) if x not in ls[0]]
    neighbors = get_neighbors(missing_ind)

    avg_list_list = []
    for i, neighbors_i in enumerate(neighbors):
        avg_list = [missing_ind[i]]
        for k in range(1, len(ls)):
            avg = sum(float(ls[k][ls[0].index(j)]) for j in neighbors_i if j in ls[0])
            avg /= len(neighbors_i)
            avg_list.append(avg)
        avg_list_list.append(avg_list)

    o = open('data-all-completed-final.csv', 'w')

    for i in range(len(avg_list_list)):
        ind2 = 0
        m = 0
        for row in ls:
            if row == ls[0]:
                ls = []
                ind2 = row.index(missing_ind[i] - 1)
            row = row[:ind2 + 1] + [avg_list_list[i][m]] + row[ind2 + 1:]
            ls.append(row)
            m += 1

    for i in range(len(ls)):
        o.writelines(','.join([str(x) for x in ls[i]]) + "\n")

    o.close()
