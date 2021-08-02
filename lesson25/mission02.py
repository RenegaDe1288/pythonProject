class Person:
    __count = 0


    def __init__(self,name,age):
        self.set_name(name)
        self.set_age(age)
        Person.__count += 1
        self.__num = Person.__count

    def __str__(self):
        try:
            print('Имя: {} и возраст:  {}'.format(self.__name,self.__age))
        except:
             print('Не все данные корректны')
             self.__age = input('Введите возраст: ')


    def set_name(self,name):
        if name.isalpha():
            self.__name = name
        else:
            print('Имя не состоист из букв')

    def set_age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
           print('Возраст не состоит из чисел')

    def get_count(self):
        return self.__count


    def get_num(self):
        return self.__num



man_1  = Person('Alex',2.3)
man_1.__str__()
man_2 = Person('Mike',56)
man_2.__str__()
man_1.__str__()
print(man_1.get_num())
print((man_2.get_num()))



