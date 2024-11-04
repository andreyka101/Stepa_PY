class Animals():
    """текст класса"""
    def __init__(self , name_loc):
        self.name = name_loc
        self.__num_priv = 9
    def get_num_priv(self):
        """текст метода"""
        return self.__num_priv
    def print_num_local(self):
        print(self.num_local)
    


dog = Animals("ggg")
# print(dog.name)
## print(dog.__num_priv)

# dog.name = 5
# print(dog.name)



# print(dog.__num_priv)
# print(dog.get_num_priv())
# dog.__num_priv = 0
# print(dog.get_num_priv())
# print(dog.__num_priv)



# dog.print_num_local()
# dog.num_local = "qwerty"
# print(dog.num_local)
# dog.print_num_local()




class Cats(Animals):
    def __init__(self, name_cat):
        super().__init__(name_cat)
        print("eeff")
        self.num_cat = 80
        self.name = self.name + "0000"

    def may_may(self):
        print("may may may")
        print(self.name , "may")



i_cat = Cats("zxv")
i_cat.may_may()