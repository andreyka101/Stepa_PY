lam_1 = lambda: 2*3
print(lam_1())


def fun_1() -> int:
    return 2*5
print(fun_1())


num = 8
lam_2 = lambda: num + 3
print(lam_2())


lam_3 = lambda x : x * 10 
print(lam_3(4))


lam_4 = lambda x , y : x + y
print(lam_4(4,9))


lam_5 = lambda x , y = 3 : x + y
print(lam_5(4))



answer = "ok" if(False) else "not"
print(answer)



lam_6 = lambda x , y : x if(x > y) else 0
print(lam_6(7 , 5))




# def fun_2(x):
#     print(x)
#     return x * 2
# arr = [1,2,3,4,5]
# arr_2 = list(map(fun_2,arr))
# print(arr_2)



# arr_3 = [1,2,3,4,5]
# arr_4 = list(map(lambda x: x * 3,arr_3))
# print(arr_4)



arr_5 = [1,2,3,4,5]
arr_6 = [1,2,3,4,5]
arr_7 = list(map(lambda x , y: x * y , arr_5 , arr_6))
print(arr_7)



arr_8 = [1,2,3,4,5,6]
arr_8 = list(filter(lambda x: x>3 ,arr_8))
print(arr_8)



arr_9 = [1,2,3,4,5,6]
arr_9 = list(map(lambda x: x*2 , filter(lambda x: x>3 ,arr_9)))
print(arr_9)



arr_10 = [
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
]
arr_10 = list(map(lambda x: list(map(lambda y: y*10 , x)) , arr_10[1]))
print(arr_10)





