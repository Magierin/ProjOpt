import connection as con
import distance as dis
import get_predicted_duration_new as gpd
import csv_to_matrix as ctm
import quantity as quan

ls = [94,209,210,522,344,222,223,329,305,517 ,350 ,481 ,524 ,189 ,190 ,495 ,226,453 ,124 ,125 ,429 ,426 ,375 ,271 ,272 ,274,441,332,234,15,516, 22,364, 276,76,428,442,508,230 ,229 ,417,430 ,418 ,409 ,313 ,312 ,275 ,173 ,174 ,284 ,335 ,386 ,301 ,405 ,161 ,162]
new_ls = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '350', '481', '524', '189', '190', '495', '226', '453', '124', '125', '429', '426', '375', '271', '272', '274', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
new_ls1 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '350', '481', '524', '189', '190', '495', '226', '453', '124', '125', '429', '426', '375', '271', '272', '274', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '442', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
new_ls2 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '350', '481', '524', '189', '190', '495', '226', '453', '124', '125', '429', '426', '375', '271', '272', '274', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
new_ls3 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '136', '444', '270', '213', '214', '520', '482', '496', '431', '497', '535', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
new_ls4 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '136', '444', '270', '213', '214', '520', '482', '496', '431', '497', '535', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
new_ls5 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '136', '444', '270', '213', '214', '520', '482', '496', '431', '497', '535', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
new_ls6 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '136', '444', '270', '213', '214', '520', '482', '511', '407', '532', '113', '531', '534', '537', '536', '516', '22', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
als = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '350', '481', '524', '189', '190', '495', '226', '453', '124', '125', '429', '426', '375', '271', '272', '274', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '442', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
als1 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '350', '481', '524', '189', '190', '495', '226', '453', '124', '125', '429', '426', '375', '271', '272', '274', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
new_ls7 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '136', '444', '270', '213', '214', '520', '482', '496', '431', '497', '535', '441', '332', '234', '15', '516', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
als_1 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '350', '481', '524', '189', '190', '495', '226', '453', '124', '125', '429', '426', '375', '271', '272', '274', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '442', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']
als_56 = ['94', '209', '210', '522', '344', '222', '223', '329', '305', '517', '350', '481', '524', '189', '190', '495', '226', '453', '124', '125', '429', '426', '375', '271', '272', '274', '441', '332', '234', '15', '516', '22', '364', '276', '76', '428', '508', '230', '229', '417', '430', '418', '409', '313', '312', '275', '173', '174', '284', '335', '386', '301', '405', '161', '162']



def get_route_duration():
    data = gpd.get_edges_predicted_duration_new(1)
    summe = 0
    for i in range(len(ls)-1):
        dic = con.get_connection(str(ls[i]), str(ls[i+1]))
        num = dic.get("number")
        summe += float(data[int(num)])
    t = float(round((round(summe, 2) - int(round(summe, 2))) * 60)) / 100 + int(round(summe, 2))
    return t


def get_routes_quantity():
    route, route_freq, k = [el[:-3] for el in ctm.csv_to_matrix('route-all.csv')], [], 0

    for i in range(len(route)):
        if route[i] not in route_freq:
            route_freq.append(route[i])

    return route_freq


ls1 = [str(x) for x in als_56]
if ls1 in get_routes_quantity():
    ind = get_routes_quantity().index(ls1)
    print(quan.get_routes_quantity()[ind])

