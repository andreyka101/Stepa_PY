
def fun_1(arr , index = 0 , summ_num = 0):
    print(arr[index])
    summ_num += arr[index]
    if(len(arr) - 1 == index):
        return summ_num
    return fun_1(arr , index + 1 , summ_num)

print(fun_1([1,2,3,4]))



def fun_2(arr_key , arr_value , index = 0 , dist_save = {}):
    if(len(arr_key) != len(arr_value)):
        return {}
    dist_save[arr_key[index]] = arr_value[index]
    if(len(arr_key) - 1 == index):
        return dist_save
    return fun_2(arr_key , arr_value , index + 1 , dist_save)

print(fun_2(["k1","k2","k3"], [1,2,3]))



