class MyDict():
    dict = {'wer': 1, 'sdf': 2}

    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return 0

    def items(self):
        list = [[k, a] for k, a in self.dict.items()]
        return list

    def keys(self):
        list = [k for k in self.dict.keys()]
        return list

    def values(self):
        list = [k for k in self.dict.values()]
        return list

    def clear(self):
        self.dict = {}
        print('Словарь очищен')

    def update(self, new_key, new_value):
        self.dict[new_key] = new_value
        return self.dict

    def pop(self, key, value = None):
        if key in self.dict:
            list = self.dict.pop(key,value)
            return list
        else:
            return value

    def popitem(self, ):
        try:
            list = self.dict.popitem()
            return list
        except:
            raise KeyError ('Словарь пуст')

dic = MyDict()

print(dic.get('we0'))
print(dic.items())
print(dic.values())
print(dic.keys())
print(dic.update('44',33))
print(dic.update('44',45))
print(dic.pop('44',45))
print(dic.pop('44',48))
print(dic.pop('wer'))
print(dic.dict)
print(dic.popitem())
dic.clear()
print(dic.popitem())



