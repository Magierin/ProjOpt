import distance as dis
import duration as dur
import parse_csv as pc
import coordinates as coo
import completing as com
import quantity as quan
import connection as con
import csv_to_matrix as ctm
import int_route_edges as ire

if __name__ == '__main__':
    """dis.get_distance_list()
    dur.get_routes_duration()
    dis.get_distance()
    pc.parse_csv()
    coo.get_coordinates()
    dis.get_distance_list()
    dis.get_edge_num_dist(469)
    com.completing()
    com.get_speed_from_neighbors()
    print(quan.get_routes_quantity_per_hour())
    dura = dur.get_routes_duration()
    print(min(dura), dura.index(min(dura)))
    dur.get_routes_duration()
    quan.get_routes_quantity()
    dis.get_edge_num_dist(0)"""
    # com.completing()
    # com.get_speed_from_neighbors()
    # geq = quan.get_edges_quantity()
    # print(geq)
    # print(quan.get_edge_quan_per())
    # dist = dis.get_distance_list()
    # print(dist[0])
    graph = pc.parse_csv()
    fro = graph[1].get('from')
    print(str(fro))

