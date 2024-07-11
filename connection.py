import parse_csv as pc

"""Returns the dictionary element from parse_csv with input 'node A' and 'node B';
mainly used for getting the edge (number) that connects A and B =>  A->B"""


def get_connection(s, f):
    p = pc.parse_csv()
    for i in range(1, len(p)):
        if ('from', str(s)) in p[i].items() and ('to', str(f)) in p[i].items():
            return p[i]


print(get_connection("209", "210"))
