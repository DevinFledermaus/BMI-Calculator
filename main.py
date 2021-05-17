# Devin Fledermaus
# BMI Calculator

from tkinter import *

# root window
from tkinter.ttk import Combobox
from tkinter import messagebox

root = Tk()
root.resizable(False, False)
root.geometry("1000x700")
root.title("BMI Calculator")


# Defining Functions
# Defining Clear Button
def clearing():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)


def button_Exit():
    msg_box = messagebox.askquestion("Terminating Program", "Are you sure you want to close this program?", icon="warning")
    if msg_box == "yes":
        root.destroy()


# Defining Calculate
def calculate():
    try:
        if cb.get() == "Male":
            height = float(e2.get())
            weight = float(e1.get())
            answer_1 = (weight / ((height / 100)*(height / 100)))
            answer_2 = (0.5 * weight / ((height / 100)*(height / 100)) + 11.5)
            e4.config(state="normal")
            e4.delete(0, END)
            e4.insert(0, answer_1)
            e4.config(state="readonly")
            e5.config(state="normal")
            e5.delete(0, END)
            e5.insert(0, answer_2)
            e5.config(state="readonly")
        elif cb.get() == "Female":
            height = float(e2.get())
            weight = float(e1.get())
            age = float(e3.get())
            answer_1 = (weight / ((height / 100)*(height / 100)))
            answer_2 = (0.5 * weight / ((height / 100)*(height / 100)) + 0.03 * age + 11)
            e4.config(state="normal")
            e4.delete(0, END)
            e4.insert(0, answer_1)
            e4.config(state="readonly")
            e5.config(state="normal")
            e5.delete(0, END)
            e5.insert(0, answer_2)
            e5.config(state="readonly")
    except ValueError as ex:
        e1.config(state="normal")
        e1.delete(0, END)
        e1.config(state="readonly")

        e2.config(state="normal")
        e2.delete(0, END)
        e2.config(state="readonly")

        e3.config(state="normal")
        e3.delete(0, END)
        e3.config(state="readonly")

        messagebox.showerror("ERROR", "Please enter all relevant information")


# Label Frame
lb = LabelFrame(root)
lb.place(x=150, y=50, width=700, height=400)


# Labels
l1 = Label(lb, text="Weight:")
l1.place(x=100, y=50)
l2 = Label(lb, text="kilogram")
l2.place(x=320, y=50)
l3 = Label(lb, text="Height:")
l3.place(x=100, y=150)
l4 = Label(lb, text="cm")
l4.place(x=320, y=150)
l5 = Label(lb, text="Gender:")
l5.place(x=100, y=250)
l6 = Label(lb, text="Age(Female only):")
l6.place(x=350, y=250)
l7 = Label(root, text="BMI:")
l7.place(x=155, y=550)
l8 = Label(root, text="Ideal BMI:")
l8.place(x=500, y=550)

# Buttons
b1 = Button(root, text="Calculate BMI and Ideal BMI", command=calculate, width=80)
b1.place(x=160, y=480)
b2 = Button(root, text="Clear", command=clearing)
b2.place(x=220, y=600)
b3 = Button(root, text="Exit", command=button_Exit)
b3.place(x=720, y=600)


# Entries
e1 = Entry(lb, width=15)
e1.place(x=180, y=50)
e2 = Entry(lb, width=15)
e2.place(x=180, y=150)
e3 = Entry(lb, width=15)
e3.place(x=480, y=250)
e4 = Entry(root, width=25, state="readonly")
e4.place(x=200, y=550)
e5 = Entry(root, width=25, state="readonly")
e5.place(x=580, y=550)
e6 = Entry(root, width=25, state="readonly")
e6.place(x=390, y=600)


# ComboBox
cb = Combobox(lb)
cb["values"] = ("Male", "Female")
cb.config(state="readonly")
cb.place(x=160, y=250)


# run program
root.mainloop()
