zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(zoo.index('kangaroo'), 'bear')
print(zoo)
zoo.remove('elephant')
print(zoo)
print('Лев сидит в клетке: ', zoo.index('lion')+1)
print('Обезьяна сидит в клетке: ', zoo.index('monkey')+1)