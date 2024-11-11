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



# open_file_2 = open("i_file.txt" , "r")
# print(open_file_2.read())



# open_file_3 = open("i_file.txt" , "w")
# print(open_file_3)
# open_file_3.write("123456789")

# open_file_3.close()

# print("open =" , open("i_file.txt" , "r").read())




# open_read = open("i_file.txt" , "r").read()
# with open("i_file.txt" , "w") as file:
#     file.write(open_read + "_5555www")

# print(open("i_file.txt" , "r").read())




# with open("i_file.txt" , "a") as file:
#     file.write("=poi")



# print("hello\n    world")
# open_read_2 = [open("i_file.txt" , "r").read()]
# print(open_read_2)



# open_read_3 = open("i_file.txt" , "r").readlines()
# print(open_read_3)



open_read_4 = open("i_file.txt" , "r").read()
arr_open_read_4 = open_read_4.split("\n")
print(arr_open_read_4)




