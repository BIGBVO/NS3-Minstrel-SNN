from scipy.stats import truncnorm

def get_truncated_normal(mean, sd, low, upp):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

X = get_truncated_normal(mean=2, sd=1, low=0.1, upp=4)
traffic_list = X.rvs(50)
proccessed_traffic_list = []

for traffic in traffic_list:
    proccessed_traffic_list.append(round(traffic, 3))

seen = []
for number in proccessed_traffic_list:
    if number in seen:
        print ("Number repeated!")
    else:
        seen.append(number)

for idx, value in enumerate(proccessed_traffic_list):
    file_name = str(idx) + ".txt"
    traffic_file = open(file_name, "w")
    traffic_file.write("0 ")
    traffic_file.write(str(value))
    traffic_file.close()

for idx, value in enumerate(proccessed_traffic_list):
    file_name = "/home/vo/Desktop/AI_Minstrel_V2/NS3_80211.ah_AI_Minstrel/Result/AI_Minstrel/FixRate/traffic_generated/" + str(idx) + ".txt"
    traffic_file = open(file_name, "w")
    traffic_file.write("traffic ")
    traffic_file.write(str(value))
    traffic_file.close()
