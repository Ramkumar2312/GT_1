
train_a = "TRAIN_A ENGINE NDL AGA AGA NGP BPL BLR BLR GHY SLM KRN"

train_b = "TRAIN_B ENGINE MAQ PNE NGP GHY GHY HYB NJP PTA NDL MAO SRR ITJ"




train_a_intermediate_stations = ['SLM', 'BLR', 'KRN']
train_b_intermediate_stations = ['SRR', 'MAQ', 'MAO', 'PNE']

def Train_At_HYD(train_txt):
    train_details = train_txt.split(' ')
    train_name = train_details[0]
    if train_name == 'TRAIN_A':
        train_Bogies = [station for station in train_details if station not in train_a_intermediate_stations]
    elif train_name == 'TRAIN_B' :
        train_Bogies = [station for station in train_details if station not in train_b_intermediate_stations]
    return train_Bogies


print(Train_At_HYD(train_b))

'''



Train_A_Distance_Details = {'CHN': 0,'SLM' : 350, 'BLR' : 550, 'KRN' : 900,
                                    'HYB' : 1200 , 'NGP' : 1600, 'ITJ' : 1900,
                                    'BPL' : 2000, 'AGA' : 2500,'NDL' : 2700 }

Train_B_Distance_Details = { 'TCV': 0, 'SRR' : 300, 'MAQ' : 600, 'MAO' : 1000,
                             'PNE': 1400, 'HYB' : 2000, 'NGP': 2400, 'ITJ': 2700,
                               'BPL': 2800, 'PTA' : 3800, 'NJP': 4200, 'GHY':4700 } '''

# for station in Train_A :
    # print(station)



'''


calculate distance from hyd 

train_a_distance = {}
print(Train_A)
for station in Train_A :
    if station in Train_A_Distance_Details :
        train_a_distance[station] = Train_A_Distance_Details[station] - 1200
print(train_a_distance)  '''
