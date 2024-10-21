


# пример работы рекурсии 1
# def fun_1(arr , index = 0 , summ_num = 0):
#     print(arr[index])
#     summ_num += arr[index]
#     if(len(arr) - 1 == index):
#         return summ_num
#     return fun_1(arr , index + 1 , summ_num)

# print(fun_1([1,2,3,4]))



# пример работы рекурсии 2
def fun_2(arr_key , arr_value , index = 0 , dist_save = {}):
    if(len(arr_key) != len(arr_value)):
        return {}
    dist_save[arr_key[index]] = arr_value[index]
    if(len(arr_key) - 1 == index):
        return dist_save
    return fun_2(arr_key , arr_value , index + 1 , dist_save)

print(fun_2(["k1","k2","k3"], [1,2,3]))




# дз
# номер 1
# Напишите функцию для вычисления факториала числа

# номер 2
# Напишите программу для возведения числа n в степень m. 
# нельзя использовать степень (**)

# номер 3
# напишите функцию которая принимает список и возвращает сумму всех чисел списка

# номер 4
# напишите функцию которая принимает два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, 
# чтобы элементы первого списка были ключами, 
# а элементы второго — соответственно значениями нашего словаря.
# функция возвращает словарь

# номер 5
# Напишите функцию которая принимает список чисел и строк и возвращает список с удалёнными строками

# номер 6
# написать функцию которая принимает строку и изменять её вставляя после каждого символа строки "^"
# пример: 
    # функция принимает "123456" 
    # функция возвращает "1^2^3^4^5^6"

# номер 7
# написать функцию которая принимает строку и число ,
#  функцию возвращает строку умноженную на число нельзя использовать умножение


# доп задачи:
# (внизу) https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23
# https://w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php



# номер 1
def fun_number_1(num , answer = 1):
    answer *= num
    num-=1
    if(num == 1):
        return answer
    else:
        return fun_number_1(num , answer)

print(fun_number_1(7))


