
# открытие файла
# open_file = open("i_file.txt")
# print(open_file)



# режимы открытия:
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись



# по умолчанию файл открывается в режиме 'r'
# open_file_2 = open("i_file.txt" , "r")
# .read() - получаем текст отрытого файла
# print(open_file_2.read())


# переписываем файл
# open_file_3 = open("i_file.txt" , "w")
# print(open_file_3)
# .write() = запись в файл
# s = "eee33"
# open_file_3.write(s)

# .close() - закрывает файл
# open_file_3.close()

# если не закрыть файл то чтение не сработает
# print("open =" , open("i_file.txt" , "r").read())




# пример перезаписи и чтения
# open_read = open("i_file.txt" , "r").read()
# with - сам закрывает файл 
# with open("i_file.txt" , "w") as file:
#     file.write(open_read + "_5555www")

# print(open("i_file.txt" , "r").read())




# пример открытия на дозапись
# with open("i_file.txt" , "a") as file:
#     file.write("=poi")




# \n - переносит строку
# print("hello\n    world")
# open_read_2 = [open("i_file.txt" , "r").read()]
# print(open_read_2)



# метод .readlines() каждую строку txt файла превращает в элемент массива
# open_read_3 = open("i_file.txt" , "r").readlines()
# print(open_read_3)



# .split(s) - разделяет строку по строке s
# open_read_4 = open("i_file.txt" , "r").read()
# arr_open_read_4 = open_read_4.split("\n")
# print(arr_open_read_4)








# with open("C:/main_brain/фаилы/del_s.txt" , encoding="UTF-8") as file:
#     print(file.read())



# with open("./pack_class/l2_file.txt" , encoding="UTF-8") as file:
#     print(file.read())



# with open("../del_file_global.txt" , encoding="UTF-8") as file:
#     print(file.read())



# with open("../../del_file_global_2.txt" , encoding="UTF-8") as file:
#     print(file.read())



# with open("../../фаилы/del_s.txt" , encoding="UTF-8") as file:
#     print(file.read())








# дз
# номер 1
# сделать программу , которая принимает текст и сохраняет в файл 


# номер 2
# сделать программу калькулятор с историей программа должна показывать историю


# номер 3
# создайте менеджер пользователей
# . программа должна работать до тех пор пока не не будет введено exit или ex
# . если ввести new - создаётся новый пользователь он должен хранить имя и пароль (если ввести существующие имя то программа просит его изменить)
# . если ввести del - удаляется пользователь его имя и пароль
# все пользователи должны сохраняются на txt файл



num_x1 = 90
print(f"qqeqe{23} iiir {num_x1}")