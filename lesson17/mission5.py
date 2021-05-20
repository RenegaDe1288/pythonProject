text = 'dsfh!^#hdsfs'
# my_text = list(text)
# new_list = []
# stop = ''
# for sym in text:
#     if sym == 'h' and stop != 'h':
#         stop = 'h'
#         index = text.index(sym)
#         for let in text[index + 1:]:
#             if let == 'h':
#                 break
#             else:
#                 new_list.append(let)
#     elif stop == 'h':
#         break
#
# print('Список символов: ', new_list[::-1])

new_text = list(text)
count = 0
for i in new_text[::-1]:
    count -= 1
    if i == 'h':
        break

my_list = [x for x in new_text[count:new_text.index('h'):-1] if x != 'h']
print('Список символов: ', my_list)
print(new_text.index('h'))
