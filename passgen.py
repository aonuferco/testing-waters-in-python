import string
from random import choice
from tkinter import *
from tkinter import ttk

bad_chars = ['I', 'l', '0', "O", "1", "o", "i"]


def generate():
    length = length_combo.get()

    if length == '':
        entry_var.set("Please choose length")
    else:
        if not symbol_var.get() and not number_var.get() and not lowerc_var.get() and not upperc_var.get():
            entry_var.set("Please choose a set")
        else:
            format_str = ""
            format_str += string.punctuation if symbol_var.get() else ""
            format_str += string.digits if number_var.get() else ""
            format_str += string.ascii_lowercase if lowerc_var.get() else ""
            format_str += string.ascii_uppercase if upperc_var.get() else ""
            if exclude_var:
                pass_str = "".join(choice("".join(filter(lambda i: i not in bad_chars, format_str))) for x in range(int(length)))
                entry_var.set(pass_str)
            else:
                pass_str = "".join(choice(format_str) for x in range(int(length)))
                entry_var.set(pass_str)


root = Tk()
root.title("python Password Generator")
root.geometry("320x230")
root.resizable(False, False)

label_length = Label(root, text="Length")
label_symbols = Label(root, text="Symbols")
label_numbers = Label(root, text="Numbers")
label_lowerc = Label(root, text="Lower case")
label_upperc = Label(root, text="Upper case")
label_exclude = Label(root, text="Exclude similar")
empty_label = Label(root, text="")
label_result = Label(root, text="Your password")

label_length.grid(row=0, sticky=W)
label_symbols.grid(row=1, sticky=W)
label_numbers.grid(row=2, sticky=W)
label_lowerc.grid(row=3, sticky=W)
label_upperc.grid(row=4, sticky=W)
label_exclude.grid(row=5, sticky=W)
empty_label.grid(row=6, sticky=W)
label_result.grid(row=7, sticky=W)

symbol_var = IntVar()
number_var = IntVar()
lowerc_var = IntVar()
upperc_var = IntVar()
exclude_var = IntVar()
entry_var = StringVar()
values = list(range(1, 31))

length_combo = ttk.Combobox(root, values=values, state="readonly")
checkbox_symbol = Checkbutton(root, text="( e.g. @#$% )", variable=symbol_var)
checkbox_number = Checkbutton(root, text="( e.g. 123456 )", variable=number_var)
checkbox_lowerc = Checkbutton(root, text="( e.g. abcdefgh )", variable=lowerc_var)
checkbox_upperc = Checkbutton(root, text="( e.g. ABCDEFGH )", variable=upperc_var)
checkbox_exclude = Checkbutton(root, text="( e.g. i, l, 1, L, o, 0, O )", variable=exclude_var)
result_entrybox = Entry(root, textvariable=entry_var)

length_combo.grid(row=0, column=1, sticky=W)
checkbox_symbol.grid(row=1, column=1, sticky=W)
checkbox_number.grid(row=2, column=1, sticky=W)
checkbox_lowerc.grid(row=3, column=1, sticky=W)
checkbox_upperc.grid(row=4, column=1, sticky=W)
checkbox_exclude.grid(row=5, column=1, sticky=W)
result_entrybox.grid(row=7, column=1, sticky=W, padx=5)

button = Button(root, text="Generate", command=generate)
button.grid(row=7, column=2, sticky=W)

root.mainloop()
