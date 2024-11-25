
num = 5
match (num):
    case(1):
        print("super 1")
    case(2):
        print("super 2")
    case(3):
        print("super 3")
    case(4):
        print("super 4")
    # case _ - действие по умолчанию (можно не писать)
    case _:
        print("default")
    

    