import  sys
input_file = sys.argv[1]
fileObject = open(input_file, "r")
data = fileObject.readlines()
data = [line.rstrip() for line in data]
print(data)
train_a = data[0]
train_b = data[1]

Train_A_Distance_Details = {'CHN': 0,'SLM' : 350, 'BLR' : 550, 'KRN' : 900,
                                    'HYB' : 1200 , 'NGP' : 1600, 'ITJ' : 1900,
                                    'BPL' : 2000, 'AGA' : 2500,'NDL' : 2700 }

Train_B_Distance_Details = { 'TCV': 0, 'SRR' : 300, 'MAQ' : 600, 'MAO' : 1000,
                             'PNE': 1400, 'HYB' : 2000, 'NGP': 2400, 'ITJ': 2700,
                               'BPL': 2800, 'PTA' : 3800, 'NJP': 4200, 'GHY':4700 } 
                               


train_a_intermediate_stations = ['SLM', 'BLR', 'KRN', 'HYB']
train_b_intermediate_stations = ['SRR', 'MAQ', 'MAO', 'PNE', 'HYB']

def Train_At_HYD(train_txt):
    train_details = train_txt.split(' ')       
    train_name = train_details[0]
    if train_name == 'TRAIN_A':
        train_Bogies = [station for station in train_details if station not in train_a_intermediate_stations]
    elif train_name == 'TRAIN_B' :
        train_Bogies = [station for station in train_details if station not in train_b_intermediate_stations]
    return train_Bogies

train_a_distance = {}


def station_distance(bogies_list):

    for station in bogies_list :
        if station in Train_A_Distance_Details.keys() :
            train_a_distance[station] = Train_A_Distance_Details[station] - 1200
        elif station in Train_B_Distance_Details.keys() :
            train_a_distance[station] = Train_B_Distance_Details[station] - 2000
    return train_a_distance

train_AB_bogies = []
engine_count = 0
final_list = []

def train_AB(train_a,train_b):
    global engine_count

    train_a_bogies = (Train_At_HYD(train_a))
    train_b_bogies = (Train_At_HYD(train_b))
    train_AB_bogies = train_a_bogies + train_b_bogies

    if train_a_bogies:
        engine_count += 1
        station_distance(train_a_bogies)
    if train_b_bogies:
        engine_count += 1
        station_distance(train_b_bogies)
    return engine_count , train_a_bogies , train_b_bogies

def final_train_AB(train_a,train_b):
    global train_AB_bogies
    engine_count , train_a_bogies , train_b_bogies = train_AB(train_a,train_b)
    train_AB_bogies = train_a_bogies + train_b_bogies
    #print(train_a_bogies)
    while train_a_distance:
        max_val = max(train_a_distance, key=train_a_distance.get)
        if max_val in train_a_distance.keys():
            for x in train_AB_bogies:
                if x == max_val:
                    final_list.append(x)
            train_a_distance.pop(max_val)

    arrival_train_a = " ".join(train_a_bogies)
    arrival_train_b = " ".join(train_b_bogies)
    departure_train_ab = " ".join(final_list)
    print(f"ARRIVAL {arrival_train_a}")
    print(f"ARRIVAL {arrival_train_b}")
    print(f"DEPARTURE TRAIN_AB {departure_train_ab}")

final_train_AB(train_a,train_b)











#arrange the station according by distance 
