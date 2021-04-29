# print('Начался 8-часовой рабочий день')
#
# count = 1
# all_task = 0
# all_calls = 0
# while count <= 8:
#     print(count, '-й час')
#     task = int(input('Сколько задач решит Максим? '))
#     all_task += task
#     count += 1
#     call = int(input('Звонит жена. Взять трубку?'))
#     if call > 0:
#         all_calls += call
# print('Рабочий день закончился. Всего выполнено задач:', all_task)
# if all_calls > 1:
#     print('Жена звонила: ', all_calls, ' раз. Нужно зайти в магазин.')

print('Начался 8-часовой рабочий день')

count = 1
all_task = 0
call = 0
while count <= 8:
    print(count, '-й час')
    task = int(input('Сколько задач решит Максим? '))
    all_task += task
    count += 1
    call = int(input('Звонит жена. Взять трубку?'))
    if call == 1:
        all_call = True
print('Рабочий день закончился. Всего выполнено задач:', all_task)
if all_call == True:
    print('Жена звонила. Нужно зайти в магазин.')
