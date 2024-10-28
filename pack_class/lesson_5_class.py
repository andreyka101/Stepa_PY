arr = [3,5,6]
print(type(arr))
arr.clear()


class Dogs():
    def __init__(self , name_local):
        print("start class Dogs")
        self.num = 9
        print(self.num)
        print(name_local)
        self.name = name_local
        self.eat_num = 0
        self.__priv_num = 8

    
    def run(self):
        print("run run run")
        # self.eat_fun()
    
    def eat_fun(self , number = 2):
        self.eat_num += number

    def get_priv_num(self):
        return self.__priv_num
    
    
    


dog_sharic = Dogs("sharic")
# print(dog_sharic.num)
# print(type(dog_sharic))


# print(dog_sharic.name)


# dog_sharic.run()


# print(dog_sharic.eat_num)
# dog_sharic.eat_fun(7)
# print(dog_sharic.eat_num)


print(dog_sharic.num)
dog_sharic.num = 3
print(dog_sharic.num)


print(dog_sharic.get_priv_num())
