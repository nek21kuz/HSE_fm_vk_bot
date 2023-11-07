def storage(file):
    with open(file  + '.txt', 'r', encoding='utf-8') as file:
        data_dict = dict.fromkeys(file.readline().split('$')[:-1])
        for i in dict.keys(data_dict):
            data_dict[i] = file.readline().split()
        return data_dict

data_music = storage('music')
data_pc = storage('pd')
data_predict = storage('prediction')
            
pl_music = list(dict.keys(data_music))
pl_pc = list(dict.keys(data_pc))
pl_predict = list(dict.keys(data_predict))
