import threading
import time



# пример без потока
# def fun():
#     print("start fun")
#     time.sleep(4)
#     print("end fun")

# fun()

# for i in range(10):
#     print(i)





# пример с потоком
def fun():
    print("start fun")
    time.sleep(4)
    print("end fun")

# threading.Thread - создание потока
thread_1 = threading.Thread(target=fun)
# .start() - запуск потока 
thread_1.start()

for i in range(10):
    print(i)

thread_1.join()
# .join() - строки ниже ждут окончание потока
print("hello")







