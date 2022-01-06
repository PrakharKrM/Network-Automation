"""
In this program i will go to write a code to create small calculator. In this i will also using from method to import
all functions of tkinter because if we use only "import tkinter" whatever module/function defined inside library
that need to be called with tkinter.*. For eg for button we call like tkinter.Button() but if we use
"from tkinter import *" then need to difine only funtion of tkinter like Button().
"""
import tkinter
from tkinter import *

def button_function_num(number):
    exist_number = input_field.get()
    input_field.delete(0, END) # it will delete any existing number and replace it with new one with previous number
    input_field.insert(0, exist_number + str(number))
    return

def clear_func():
    input_field.delete(0, END)
    return

def addition():
    global number1
    number1 = int(input_field.get())  # Store number at one place and then add
    input_field.delete(0, END) # This will clear input field to enter another number
    global operator
    operator = "+"
    return

def substraction():
    global number1
    number1 = int(input_field.get())  # Store number at one place and then add
    input_field.delete(0, END) # This will clear input field to enter another number
    global operator
    operator = "-"
    return

def multiplication():
    global number1
    number1 = int(input_field.get())  # Store number at one place and then add
    input_field.delete(0, END) # This will clear input field to enter another number
    global operator
    operator = "*"
    return

def division():
    global number1
    number1 = int(input_field.get())  # Store number at one place and then add
    input_field.delete(0, END) # This will clear input field to enter another number
    global operator
    operator = "/"
    return

def equal():
    global number2
    number2 = input_field.get()
    if operator == "+":
        number3 = float(number1) + float(number2)
        input_field.delete(0, END)
        input_field.insert(0, str(number3))
    elif operator == "-":
        number3 = float(number1) - float(number2)
        input_field.delete(0, END)
        input_field.insert(0, str(number3))
    elif operator == "*":
        number3 = float(number1) * float(number2)
        input_field.delete(0, END)
        input_field.insert(0, str(number3))
    elif operator == "/":
        number3 = float(number1) / float(number2)
        input_field.delete(0, END)
        input_field.insert(0, str(number3))
    return



tk_main_window = Tk()

tk_main_window.title("Calculator")

# Define input field for numbers and operation and place it.

input_field = Entry(tk_main_window, borderwidth=3, bg="black", fg="white")
input_field.grid(row=0, column=0, columnspan=3,rowspan=2, pady=30, padx=50)
input_field.get()

# Define buttons for numbers
button_1 = Button(tk_main_window, text="1", padx=30, pady=30, command= lambda: button_function_num(1))
button_2 = Button(tk_main_window, text="2", padx=30, pady=30, command= lambda: button_function_num(2))
button_3 = Button(tk_main_window, text="3", padx=30, pady=30, command= lambda: button_function_num(3))
button_4 = Button(tk_main_window, text="4", padx=30, pady=30, command= lambda: button_function_num(4))
button_5 = Button(tk_main_window, text="5", padx=30, pady=30, command= lambda: button_function_num(5))
button_6 = Button(tk_main_window, text="6", padx=30, pady=30, command= lambda: button_function_num(6))
button_7 = Button(tk_main_window, text="7", padx=30, pady=30, command= lambda: button_function_num(7))
button_8 = Button(tk_main_window, text="8", padx=30, pady=30, command= lambda: button_function_num(8))
button_9 = Button(tk_main_window, text="9", padx=30, pady=30, command= lambda: button_function_num(9))
button_0 = Button(tk_main_window, text="0", padx=30, pady=30, command= lambda: button_function_num(0))
button_clear = Button(tk_main_window, text="Clear", padx=30, pady=30, command= clear_func)
button_add = Button(tk_main_window, text="+", padx=30, pady=30, command= addition)
button_sub = Button(tk_main_window, text="-", padx=30, pady=30, command= substraction)
button_mult = Button(tk_main_window, text="*", padx=30, pady=30, command= lambda: multiplication())
button_div = Button(tk_main_window, text="/", padx=30, pady=30, command= lambda: division())
button_equal = Button(tk_main_window, text="=", padx=30, pady=30, bg="green",
                      command= lambda: equal())

# Place buttons on screen
button_9.grid(row=2, column=0, padx=30)
button_8.grid(row=2, column=1, padx=30)
button_7.grid(row=2, column=2, padx=30)

button_6.grid(row=3, column=0, padx=30)
button_5.grid(row=3, column=1, padx=30)
button_4.grid(row=3, column=2, padx=30)

button_3.grid(row=4, column=0, padx=30)
button_2.grid(row=4, column=1, padx=30)
button_1.grid(row=4, column=2, padx=30)

button_0.grid(row=5, column=0, padx=30)
button_clear.grid(row=5, column=1, padx=30)
button_div.grid(row=5, column=2, padx=30)

button_add.grid(row=6, column=0, padx=30)
button_sub.grid(row=6, column=1, padx=30)
button_mult.grid(row=6, column=2, padx=30)
button_equal.grid(row=7, column=0, padx=30, columnspan=3)


tk_main_window.mainloop()
