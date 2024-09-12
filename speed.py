import completing as com
import csv_to_matrix as ctm

'''Takes file and a number; creates a new data_all csv file'''


def get_speed_from_neighbors(data, num):
    ls = ctm.csv_to_matrix(data)

    for i in range(len(ls[0]) - 3):  # macht die edge names von string zu int
        ls[0][i] = int(ls[0][i])

    missing_ind = [x for x in range(1, 1310) if x not in ls[0]]  # liste der fehlenden indices
    neighbors = com.get_neighbors(missing_ind)  # edge names der nachbarn der edge names, die fehlen

    ind = [i for i in range(len(neighbors)) if len(neighbors[i]) == 0]  # indices für missing edge names, die nicht ex.
    neighbors_new = [a for a in neighbors if len(a) != 0]  # Nachbarn für missing edge names, die existieren

    j = 0
    for i in range(len(ind)):  # entfernt die edge names, die nicht existieren
        ind[i] -= j
        del missing_ind[ind[i]]
        j += 1

    avg_list_list = []
    for i, neighbors_i in enumerate(neighbors_new):
        avg_list = [missing_ind[i]]
        for k in range(1, len(ls)):
            avg = sum(float(ls[k][ls[0].index(j)]) for j in neighbors_i if j in ls[0])
            avg /= len(neighbors_i)
            avg_list.append(avg)
        avg_list_list.append(avg_list)

    o = open('data-all-final-new-{num}.csv'.format(num=num), 'w')

    for i in range(len(avg_list_list)):
        ind2 = 0
        m = 0
        for row in ls:
            if row == ls[0]:
                ls = []
                if missing_ind[i] - 1 not in missing_ind:
                    for q in range(1, 30):
                        if missing_ind[i] - q in row:
                            ind2 = row.index(missing_ind[i] - q)
                            break
                else:
                    ind2 = row.index(missing_ind[i] - 1)
            row = row[:ind2+1] + [avg_list_list[i][m]] + row[ind2+1:]
            ls.append(row)
            m += 1

    for i in range(len(ls)):
        o.writelines(','.join([str(x) for x in ls[i]]) + "\n")

    o.close()


'''Creates data-all-final-new.csv'''


def create_data_all_final_new():
    get_speed_from_neighbors('data-all.csv', 0)
    for z in range(1, 7):
        get_speed_from_neighbors('data-all-final-new-{num}.csv'.format(num=z-1), z)
