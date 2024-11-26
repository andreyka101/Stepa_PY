from array import array


# создаём массив
# array(r , s)
# r - режим массива (размер каждой ячейки в массиве , таблица в ссылке)
# s - список (можно не писать)
arr = array('b' , [6,2,5,1])
print(arr)
# print(arr[0])



# array.append(х) - добавление элемента в конец массива.
# array.count(х) - возвращает количество вхождений х в массив.
# array.extend(arr_x) - добавление элементов из списка в массив.
# array.index(х) - номер первого вхождения x в массив.
# arr.insert(2, 99)# - включить новый пункт со значением х в массиве перед номером n. Отрицательные значения рассматриваются относительно конца массива.
# print(arr)
# array.pop(i) - удаляет i-ый элемент из массива и возвращает его. По умолчанию удаляется последний элемент.
# array.remove(х) - удалить первое вхождение х из массива.
# array.reverse() - обратный порядок элементов в массиве.




# возвращает режим массива (символ при создании массива)
# print(arr.typecode)



# размер в байтах каждого элемента в массиве
# print(arr.itemsize)



# кортеж (ячейка памяти, длина масива). Полезно для низкоуровневых операций.
# print(arr.buffer_info())



# изменяет порядок следования байтов в каждом элементе массива.
# arr.byteswap()
# print(arr)



# .fromlist() - добавление элементов из списка
# arr.fromlist([12,14,16])
# print(arr)



# .tolist() - преобразование массива в список
# arr_list = arr.tolist()
# print(arr_list)
# print(arr)



# .tobytes() - преобразовывает к байтам
# print(arr.tobytes())



# frombytes(x) - делает массив из байт
# bytes(b, r) - превращает строку (b) в байты для работы нужно указать кодировку (r)
# arr.frombytes(bytes('\x11\x90\x00' , encoding="UTF-8"))
# print(arr , "🐌")



# .tofile(f) - сохраняет массив в открытый файл (f) , файл сохраняется в байтах
# with open("arr_file.txt" , "bw" ) as file:
#     arr.tofile(file)



# .fromfile(f , n) - записывает (n) чисел из (f) файла в массив , числа в файле должны быть в байтах
# with open("arr_file.txt" , "br" ) as file:
#     arr_2 = array("b")
#     arr_2.fromfile(file , 2)
#     print(arr_2)





# сортировка пузырьком
def sort_arr(arr_loc):
    for i in arr_loc:
        for index in range(len(arr_loc) - 1):
            if(arr_loc[index] > arr_loc[index + 1]):
                # element = arr_loc[index]
                # arr_loc[index] = arr_loc[index + 1]
                # arr_loc[index + 1] = element

                arr_loc[index],  arr_loc[index + 1] = arr_loc[index + 1],  arr_loc[index]
    
    return arr_loc

print(sort_arr(arr))


