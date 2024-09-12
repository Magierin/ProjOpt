import quantity as quan

perc = []
routes = quan.get_routes_quantity_per_hour()

for i in range(24):
    percentages = quan.get_edges_quan_per_hour_percentage(routes[i])
    perc.append(percentages)
