family_member = {
    "names": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

# for i in family_member:
#     print(i, ' : ', family_member[i])
#
# if "name" in family_member:
#     print(family_member["name"])
#
# print(family_member.get('chldren', {}).get('name'))
check = 'Bob'
for i in family_member.get("children"):
    if i.get('name') == check:
        print('имя {} есть в списке детей'. format(check))
        break
else:
    print('Имя отсутствует в списке')