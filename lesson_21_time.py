import time

# https://codelessons.dev/ru/rand-in-cplusplus/


# .time() - получить unix время
# print(time.time())
start = 1
end = 20
# формула рандомного числа
print(int(time.time() % (end - start + 1) + start))



# .sleep(s) - программа останавливается на s секунд
# print(time.time())
# time.sleep(3)
# print(time.time())





import datetime

# data_time_now = datetime.datetime.now()


# получаем дату и время
# print(data_time_now)



# получаем дату
# print(data_time_now.date())
# print(data_time_now.date().day)



# получаем время
# print(data_time_now.time())
# print(data_time_now.time().minute)
# print(data_time_now.time().second)
# print(data_time_now.time().microsecond)




