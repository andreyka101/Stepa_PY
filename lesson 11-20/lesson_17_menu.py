from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("400x400")
window.config(bg="#ffec19")



num_menu = Menu(tearoff=0)
num_menu.add_command(label="1")
num_menu.add_command(label="2")
num_menu.add_command(label="3")



main_menu = Menu()
def fun():
    window.config(bg="#19ffb6")
main_menu.add_command(label="butt" , command=fun)


file_menu = Menu(tearoff= 0)

file_menu.add_command(label="open")

num_check = IntVar()
file_menu.add_checkbutton(label="check" , variable=num_check)

file_menu.add_separator()

num_radio = IntVar()
file_menu.add_radiobutton(label="radio 1" , variable=num_radio , value=1)
file_menu.add_radiobutton(label="radio 2" , variable=num_radio , value=2)
file_menu.add_radiobutton(label="radio 3" , variable=num_radio , value=3)

file_menu.add_cascade(label="num" , menu=num_menu)




main_menu.add_cascade(label="file" , menu=file_menu)
main_menu.add_cascade(label="num" , menu=num_menu)



window.config(menu=main_menu)
window.mainloop()