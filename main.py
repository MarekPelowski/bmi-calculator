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

weight_reminder = Label(root, text="kilograms", font=("consolas", 18, "italic"), bg="lightblue")
weight_reminder.place(x=375, y=30)


height_label = Label(root, text="height", font=("consolas", 18), bg="lightblue")
height_label.place(x=20, y=80)

height_entry = Entry(root, font=("consolas", 18))
height_entry.place(x=110, y=80)

height_reminder = Label(root, text="meters", font=("consolas", 18, "italic"), bg="lightblue")
height_reminder.place(x=375, y=80)

calculation_button = Button(root, text="calculate", font=("consolas", 15), bg="white")
calculation_button.place(x=20, y=140)


root.mainloop()