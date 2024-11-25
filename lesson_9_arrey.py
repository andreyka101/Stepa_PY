from array import array

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



# print(arr.typecode)



# print(arr.itemsize)



# print(arr.buffer_info())



# arr.byteswap()
# print(arr)



# arr.fromlist([12,14,16])
# print(arr)



# arr_list = arr.tolist()
# print(arr_list)
# print(arr)



# print(arr.tobytes())



# arr.frombytes(bytes('\x11\x90\x00' , encoding="UTF-8"))
# print(arr , "🐌")



# with open("arr_file.txt" , "bw" ) as file:
#     arr.tofile(file)



# with open("arr_file.txt" , "br" ) as file:
#     arr_2 = array("b")
#     arr_2.fromfile(file , 2)
#     print(arr_2)





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


