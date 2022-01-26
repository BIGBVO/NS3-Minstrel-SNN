import numpy as np 

number_of_sta = 16
lower_bound_v = 1
higher_bound_v = 10
total_traffic = 1.6

v_total = 0
v_list = []
traffic_list = []


for num in range(number_of_sta):
    v = np.random.uniform(lower_bound_v, higher_bound_v)
    v_list.append(v)
    v_total += v

for data in v_list:
    traffic = (total_traffic*data)/v_total
    traffic_list.append(traffic)

file_name = str(number_of_sta) + "_" + str(round(total_traffic,2)) + ".txt"

f = open(file_name, "w")

for idx, data in enumerate(traffic_list):
    f.write(str(idx) + "\t" + str(data) + "\n")

f.close()
