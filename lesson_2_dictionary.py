obj = {
    "key": 70,
    "5":5,
    6:"45"
}
print(obj)
print(obj["5"])
obj["5"] = 20
print(obj["5"])
obj["33"] = 999
print(obj["33"])




arr_obj = {
    0:"q",
    1:"w",
    2:"e",
    3:"r",
}
print(arr_obj[1])
print(type(arr_obj))




# obj.clear()
print(obj)



obj_2 = obj.copy()
print(obj_2)



print(obj.get("qwerty"))



obj.setdefault("qwerty" , "ouo")
print(obj)



print(obj.keys())



print(obj.values())



print(obj.pop("qwerty"))
print(obj)



obj.popitem()
print(obj)



obj.update({"zxd":5})
print(obj)



print(obj.items())
# for i in obj:
#     print(i)
for key_index , value_index in obj.items():
    print(key_index , "=" ,value_index)



str_num = "u"

if(str_num == "q"):
    print("ok q")
elif(str_num == "w"):
    print("ok w")
elif(str_num == "e"):
    print("ok e")
elif(str_num == "r"):
    print("ok r")
elif(str_num == "t"):
    print("ok t")



if_dist_obj = {
    "q": "ok q",
    "w": "ok w",
    "e": "ok e",
    "r": "ok r",
    "t": "ok t",
}
print(if_dist_obj[str_num])

