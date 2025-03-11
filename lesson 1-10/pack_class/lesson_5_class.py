
# классы везде
arr = [3,5,6]
print(type(arr))
arr.clear()


class Dogs():
    # init - вызывается при создании класса
    # self - это хранилище переменных и методов
    def __init__(self , name_local):
        print("start class Dogs")
        # создание переменной
        self.num = 9
        # использование переменной
        print(self.num)
        print(name_local)
        self.name = name_local
        self.eat_num = 0
        # пишем в начале __ для создания приватной переменной или метода
        self.__priv_num = 8

    # создание метода
    def run(self):
        print("run run run")
        # self.eat_fun()
    
    # метод изменяет переменную
    def eat_fun(self , number = 2):
        self.eat_num += number

    # способ получения приватной переменной
    def get_priv_num(self):
        return self.__priv_num
    
    
    

# создание объекта (вызов класса)
dog_sharic = Dogs("sharic")
# print(dog_sharic.num)
# print(type(dog_sharic))


# получаем переменную класса
# print(dog_sharic.name)



# вызываем метод
# dog_sharic.run()


# print(dog_sharic.eat_num)
# метод меняет переменную eat_num
# dog_sharic.eat_fun(7)
# print(dog_sharic.eat_num)


print(dog_sharic.num)
# меняем переменную класса
dog_sharic.num = 3
print(dog_sharic.num)


print(dog_sharic.get_priv_num())






# дз

# номер 1
# создайте класс с тремя переменными 
# у класса есть метод который возвращает все переменные в списке

# номер 2
# Создать класс, описывающий автомобиль (производитель, 
# модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации об автомобиле.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# номер 3
# создать класс колькулятор 
# в конструкторе нужно в писать 2 числа
# создать 4 метода: умножение , деление , сумма , вычитание
# создать метод для добавления числа (его можно вызвать много раз и подучить много чисел)
