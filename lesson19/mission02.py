info = input('Введите информацию о студенте:\n Имя, фамилию, город, место учебы, оценки:').split()
info_dict = dict()
info_dict['Имя'] = info[0]
info_dict['фамилия'] = info[1]
info_dict['город'] = info[2]
info_dict['место учебы'] = info[3]
info_dict['оценки'] = info[4::]
for key in info_dict:
    print(key, ' - ', info_dict[key])
