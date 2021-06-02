def depth(tree, key_1):
    count = 0
    while (tree[key_1]) is not None:
        if key_1 in tree:
            key_1 = tree[key_1]
            count += 1
    return count


n = int(input('Введите количество человек: '))
tree = dict()
for i in range(1, n):
    print('{} пара: '.format(i))
    child, parent = input('').split()
    tree[child] = parent
    if parent not in tree:
        tree[parent] = None
for key, value in sorted(tree.items()):
    print(key, depth(tree, key))

print(tree)
