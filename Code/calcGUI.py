    # Tom Collier
#15/09/2022

# **************************************************
# Python calclator with GUI (Graphic User Interface)
# ***************************************************

from ctypes.wintypes import RGB
from tkinter import *
from turtle import color # import everything from  the tkinter library

# Declaring variables

num_colour = "lightcyan1"

num2_colour = "lightcyan2"
op_colour = "turquoise"

text_colour="grey15"

def button_press(num): # Defining each button press
    global equation_text
    
    equation_text = equation_text + str(num)
    
    equation_label.set(equation_text)

def equals():  # This block checks for the button_press(equals)
    
    global equation_text
    
    try:  # try is used to try... except blocks. It defines a block of code tests if it contains any errors.
          # You can define different blocks for different error types, and blocks to ececute if nothing went wrong
        total = str(eval(equation_text)) # pases the expression argument and ealuates it as a python ecpression.
        
        equation_label.set(total) 
        
        equation_text = total
        
    except SyntaxError: # Check for syntax error
        
        equation_label.set("SYNTAX ERROR")
        
        equation_text = ""
        
    except ZeroDivisionError: # Check for division by zero
        
        equation_label.set("MATH ERROR")
        
        equation_text = ""
        
def clear(): # Clears the equation_label for the next calculation
    global equation_text
    
    equation_label.set("")
    
    equation_text = ""

window =Tk()
window.title("Python Calculator")
window.geometry("433x610")
window.configure(bg="cornflowerblue")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("console", 30), bg="cadetblue2", width=100, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(8))
button8 .grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, fg=text_colour, bg= num_colour, activebackground= num2_colour, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, fg=text_colour, bg=num_colour, activebackground= num2_colour, command=lambda: button_press(0))
button0.grid(row=3, column=0)

# Create the operation buttons

plus = Button(frame, text='+', height=9, width=9, font=35, fg=text_colour, bg= op_colour, command=lambda: button_press('+'))
plus.grid(row=2, column=3, rowspan=2)

minus = Button(frame, text='-', height=4, width=9, font=35, fg=text_colour, bg= op_colour, command=lambda: button_press('-'))
minus.grid(row=3, column=2)

multiply = Button(frame, text='×', height=4, width=9, font=35, fg=text_colour, bg= op_colour, command=lambda: button_press('*'))
multiply.grid(row=1, column=3)

divide = Button(frame, text='÷', height=4, width=9, font=35, fg=text_colour, bg= op_colour, command=lambda: button_press('/'))
divide.grid(row=0, column=3)

# Create equals

equal = Button(frame, text='=', height=4, width=9, font=35, fg=text_colour, bg = op_colour, command=equals)
equal.grid(row=4, column=3)

# Create decimal
 
decimal = Button(frame, text='.', height=4, width=9, font=35,  fg=text_colour, bg = op_colour, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='Clear', height=50, width=50,  fg=text_colour, bg = op_colour, font=35, command=clear)
clear.pack()



window.mainloop()