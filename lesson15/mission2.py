new_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new = []
for index in range(1, len(new_list), 2):
    new.append(new_list[index])
print(new)
print(len(new_list))

