import parse_csv as pc

"""Returns the dictionary element from parse_csv with input 'node A' and 'node B';
mainly used for getting the edge (number) that connects A and B =>  A->B"""


def get_connection(s, f):
    p = pc.graph
    for i in range(1, len(p)):
        if ('from', s) in p[i].items() and ('to', f) in p[i].items():
            return p[i]
