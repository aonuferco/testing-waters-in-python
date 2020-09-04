from tkinter import *

str_var = ""


def press(num):
    global str_var
    str_var = str_var + str(num)
    equation.set(str_var)


def equals():
    try:
        global str_var
        total = equation.get()
        equation.set(str(eval(total)))
        str_var = ""
    except:
        equation.set("Error")


def clear():
    global str_var
    str_var = ""
    equation.set("")


root = Tk()
root.title("python Calculator")
root.geometry("380x295")
root.resizable(False, False)
#entry
equation = StringVar()
expression_entry = Entry(root, textvariable=equation, bd=5, width=55).grid(row=0, column=0, columnspan=4, padx=10,
                                                                           pady=5)

button_1 = Button(root, text="1", command=lambda: press(1), padx=40, pady=20).grid(row=3, column=0)
button_2 = Button(root, text="2", command=lambda: press(2), padx=40, pady=20).grid(row=3, column=1)
button_3 = Button(root, text="3", command=lambda: press(3), padx=40, pady=20).grid(row=3, column=2)
button_4 = Button(root, text="4", command=lambda: press(4), padx=40, pady=20).grid(row=2, column=0)
button_5 = Button(root, text="5", command=lambda: press(5), padx=40, pady=20).grid(row=2, column=1)
button_6 = Button(root, text="6", command=lambda: press(6), padx=40, pady=20).grid(row=2, column=2)
button_7 = Button(root, text="7", command=lambda: press(7), padx=40, pady=20).grid(row=1, column=0)
button_8 = Button(root, text="8", command=lambda: press(8), padx=40, pady=20).grid(row=1, column=1)
button_9 = Button(root, text="9", command=lambda: press(9), padx=40, pady=20).grid(row=1, column=2)
button_0 = Button(root, text="0", command=lambda: press(0), padx=40, pady=20).grid(row=4, column=0)

button_plus = Button(root, text="+", command=lambda: press("+"), padx=30, pady=20).grid(row=4, column=3, sticky="nsew")
button_minus = Button(root, text="-", command=lambda: press("-"), padx=40, pady=20).grid(row=3, column=3)
button_multiply = Button(root, text="*", command=lambda: press("*"), padx=40, pady=20).grid(row=2, column=3)
button_divide = Button(root, text="/", command=lambda: press("/"), padx=40, pady=20).grid(row=1, column=3)

button_clear = Button(root, text="C", command=clear, padx=30, pady=20).grid(row=4, column=1, sticky="nsew")
button_equals = Button(root, text="=", command=equals, padx=30, pady=20).grid(row=4, column=2, sticky="nsew")

root.mainloop()
