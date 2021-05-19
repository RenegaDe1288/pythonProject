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

def end_of_loop():
    return StopIteration

new_text = list(text)
my_list = [x if x != 'h' else end_of_loop() for x in new_text[new_text.index('h'):] ]
print('Список символов: ', my_list[::-1])
print(new_text.index('h'))
