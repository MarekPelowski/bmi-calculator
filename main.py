from tkinter import *

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg="lightblue")
root.title("bmi calculator")
root.iconbitmap("questhead")


weight_label = Label(root, text="weight", font=("consolas", 18), bg="lightblue")
weight_label.place(x=20, y=30)

weight_entry = Entry(root, font=("consolas", 18))
weight_entry.place(x=110, y=30)

root.mainloop()