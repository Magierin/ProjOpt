import csv_to_matrix as ctm
import quantity as quan

'''Returns list with timestamps from '28 Mr 00_09_46' to '11 Mai 23_54_11' '''


def get_timestamp():
    data = ctm.data_all_final_new
    test_data = ctm.route_all_missing_last_day
    stamp = []

    for i in range(1, len(test_data)+1):
        stamp.append(' '.join(data[i][len(data[i])-3:]))

    return stamp


'''Returns list with timestamps from '28 Mr 00_09_46' to '8 Apr 04_45_36' '''


def get_timestamp_val():
    data = ctm.data_all_final_new
    test_data = ctm.route_all_missing_last_day[3212:]
    stamp = []

    for i in range(1, len(test_data)+1):
        stamp.append(' '.join(data[i][len(data[i])-3:]))

    return stamp


'''Takes timestamp in form of '28 Mar 00_09_47'; returns list with historical routes taken in this hour'''


def get_timestamp_route_list(timestamp):
    ts = timestamp.split()
    hour = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23']

    ls = []
    for i in hour:
        if ts[2].startswith(i):
            ls = quan.get_routes_quantity_per_hour()[hour.index(i)]
            break

    return ls


'''Returns list with timestamps from '28 Mr 00_09_46' to '12 Mai 23_56_09' '''


def get_timestamp_all():
    data = ctm.data_all_final_new
    stamp = []

    for i in range(1, len(data)):
        stamp.append(' '.join(data[i][len(data[i])-3:]))

    return stamp


'''Takes timestamp in form of '28 Mar 00_09_47'; returns list with all speeds from this timestamp'''


def get_speed_from_timestamp(timestamp):
    stamps = get_timestamp_all()
    speed = 0

    for i in range(len(stamps)):
        if stamps[i] == timestamp:
            speeds = ctm.data_all_final_new[i + 1]
            for j in range(len(speeds)-3):
                speed += float(speeds[j])
            duration = speed/len(speeds)
            return duration
