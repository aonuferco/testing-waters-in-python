from tkinter import *
import time
from tkinter import messagebox


def start():
    total_time = (int(hrs_var.get()) * 3600) + (int(min_var.get()) * 60) + int(sec_var.get())
    while total_time > -1:
        mins, secs = divmod(total_time, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        text_label['text'] = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)

        root.update()
        time.sleep(1)

        if total_time == 0:
            messagebox.showinfo("python Timer", "Time is up ")

        total_time -= 1


root = Tk()
root.title("python Timer")
root.geometry("250x100")
root.resizable(False, False)


text_label = Label(root, text="Select time for countdown")
text_label.grid(column=3, columnspan=5)

hrs_list = list(range(0, 24))
min_list = list(range(0, 60))
sec_list = list(range(0, 60))

hrs_var = StringVar()
hrs_var.set("0")
min_var = StringVar()
min_var.set("0")
sec_var = StringVar()
sec_var.set("0")

hrs_label = Label(root, text="Hrs").grid(row=1, column=2)
min_label = Label(root, text="Min").grid(row=1, column=4)
sec_label = Label(root, text="Sec").grid(row=1, column=6)
empty = Label(root, text="").grid(row=2)

hrs_menu = OptionMenu(root, hrs_var, *hrs_list).grid(row=1, column=3)
min_menu = OptionMenu(root, min_var, *min_list).grid(row=1, column=5)
sec_menu = OptionMenu(root, sec_var, *sec_list).grid(row=1, column=7)

btn_start = Button(root, text="Start", command=start, width=5).grid(row=3, column=5)

root.mainloop()
