from tkinter import *
clicks = 0
def click():
    global clicks
    clicks += 1
    print(clicks)
    label.config(text = clicks)

window = Tk()
window.title("Кликер")
window.geometry("300x200")

click_button = Button(text="Клик", command=click)
click_button.pack()

label = Label(text=clicks)
label.pack()

window.mainloop()