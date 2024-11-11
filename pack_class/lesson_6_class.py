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




# наследуем класс Animals
# в наследуемом классе можно создавать свои переменные и методы
class Cats(Animals):
    def __init__(self, name_cat , num_s_cat):
        # вызываем метод родителя
        super().__init__(name_cat)
        print("eeff")
        self.num_cat = 80
        self.num_s_cat = num_s_cat
        self.name = self.name + "0000"

    def may_may(self):
        print("may may may")
        print(self.name , "may")



i_cat = Cats("zxv" , 3)
i_cat.may_may()





# дз
# задание 1
# создайте родительский класс , описывающий транспорт
# (модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации о транспорте.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# наследуйте класс автомобили в котором есть ещё одна переменная количество мест

# наследуйте класс вертолеты с дополнительным методом взлет 



class All_big_class():
    def __init__(self , nume , num):
        self.cats = Cats(nume , num)
        self.animals = Animals(nume)


big_num = All_big_class("wwww" , 8)
print(big_num.animals.name)
big_num.cats.may_may()


