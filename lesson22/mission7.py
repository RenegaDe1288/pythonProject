file_1 = open('first_tour.txt', 'r', encoding='utf-8')
copy_file = (open('second_tour.txt', 'w', encoding='utf-8'))

text = file_1.read().split('\n')
min_points = int(text[0])
text = text[1::]

#  Решение №2 со списком

points_list = sorted([line.split()[2] for line in text if min_points < int(line.split()[2])], reverse=True)
copy_file.write(str(len(points_list)))


for i, points in enumerate(points_list):
    for line in text:
        if points in line:
            string = '\n' + str(i + 1) + ') ' + line.split()[1][0] + '. ' + line.split()[0] + ' ' + points
            copy_file.write(string)

file_1.close()
copy_file.close()


# Решение №1 со словарем

game_dict = {}

for line in text:
    data = line.split()
    if min_points < int(data[2]):
        game_dict[data[2]] = data[1][0] + '.' + data[0]

copy_file.write(str(len(game_dict)))

for i, key in enumerate(sorted(game_dict, reverse=True)):
    string = '\n' + str(i+1) + ') ' + game_dict[key] + ' ' + key
    copy_file.write(string)

file_1.close()
copy_file.close()
