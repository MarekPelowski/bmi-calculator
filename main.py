from tkinter import *

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg="lightblue")
root.title("bmi calculator")
root.iconbitmap("questhead")

def calculation():

    weight = weight_entry.get()
    height = height_entry.get()

    bmi = float(weight) / (float(height) * float(height))

    bmi = round(bmi, 3)

    weight_label.destroy()
    weight_entry.destroy()
    weight_reminder.destroy()
    height_label.destroy()
    height_entry.destroy()
    height_reminder.destroy()
    calculation_button.destroy()

    body_mass_var = StringVar()
    body_mass_var.set("")

    bmi_label = Label(root, text="Your body mass index is: ", font=("Times new roman", 25), bg="lightblue")
    bmi_label.place(x=20, y=60)

    bmi_text = Label(root, text=(bmi), font=("consolas", 40), bg="lightblue", fg="darkblue")
    bmi_text.place(x=40, y=100)

    bmi_body_mass = Label(root, text="You are:", font=("Times New Roman", 25), bg="lightblue")
    bmi_body_mass.place(x=20, y=250)

    bmi_body_mass_text = Label(root, textvariable=body_mass_var, font=("consolas", 25), bg="lightblue",  fg="darkblue")
    bmi_body_mass_text.place(x=20, y=290)

    if bmi < 18.5:

        body_mass_var.set("UNDERWEIGHT")

    elif bmi >= 18.5 and bmi <= 24.9:

        body_mass_var.set("NORMAL")

    elif bmi >= 25 and bmi <= 29.9:

        body_mass_var.set("OVERWEIGHT")

    elif bmi >= 30 and bmi <= 34.9:

        body_mass_var.set("FAT")

    elif bmi >= 35:

        body_mass_var.set("EXTREMELY FAT")

weight_label = Label(root, text="weight", font=("consolas", 18), bg="lightblue")
weight_label.place(x=20, y=30)

weight_entry = Entry(root, font=("consolas", 18))
weight_entry.place(x=110, y=30)

weight_reminder = Label(root, text="kilograms", font=("consolas", 15, "italic"), bg="lightblue")
weight_reminder.place(x=380, y=30)


height_label = Label(root, text="height", font=("consolas", 18), bg="lightblue")
height_label.place(x=20, y=80)

height_entry = Entry(root, font=("consolas", 18))
height_entry.place(x=110, y=80)

height_reminder = Label(root, text="meters", font=("consolas", 15, "italic"), bg="lightblue")
height_reminder.place(x=380, y=80)

calculation_button = Button(root, text="calculate", font=("consolas", 15), bg="white", command=calculation)
calculation_button.place(x=20, y=140)


root.mainloop()