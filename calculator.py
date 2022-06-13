from tkinter import *

root = Tk()
root.title("Calculator")

i = 0

#.grid -> position of elements in the window. padx-> space between window and widget
#
#Entry-> Name of our widget
e_text = Entry(root, font= ("Calibri 20"))
e_text.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5) 

# #Functions
def click_button(value):
    global i
    e_text.insert(i, value)
    i += 1
    return
    
def erase():
    e_text.delete(0, END)
    i = 0

def calculate():
    equation = e_text.get() 
    results = eval(equation)
    e_text.delete(0, END)
    e_text.insert(0,results)
    i = 0

# #buttons 

button1 = Button(root, text = "1", width = 5, height = 2,command = lambda: click_button(1))
button2 = Button(root, text = "2", width = 5, height = 2,command = lambda: click_button(2)) 
button3 = Button(root, text = "3", width = 5, height = 2,command = lambda: click_button(3))
button4 = Button(root, text = "4", width = 5, height = 2,command = lambda: click_button(4))
button5 = Button(root, text = "5", width = 5, height = 2,command = lambda: click_button(5))
button6 = Button(root, text = "6", width = 5, height = 2,command = lambda: click_button(6))
button7 = Button(root, text = "7", width = 5, height = 2,command = lambda: click_button(7))
button8 = Button(root, text = "8", width = 5, height = 2,command = lambda: click_button(8))
button9 = Button(root, text = "9", width = 5, height = 2,command = lambda: click_button(9))
button0 = Button(root, text = "0", width = 19, height = 2,command = lambda: click_button(0))

button_erase = Button(root, text = "AC", width = 5, height = 2,command = lambda: erase())
button_parenthesis1= Button(root, text = "(", width = 5, height = 2,command = lambda: click_button("("))
button_parenthesis2 = Button(root, text = ")", width = 5, height = 2,command = lambda: click_button(")"))
button_point = Button(root, text = ".", width = 5, height = 2,command = lambda: click_button("."))

button_div = Button(root, text = "/", width = 5, height = 2,command = lambda: click_button("/"))
button_mult = Button(root, text = "x", width = 5, height = 2,command = lambda: click_button("*"))
button_sum = Button(root, text = "+", width = 5, height = 2,command = lambda: click_button("+"))
button_subtract = Button(root, text = "-", width = 5, height = 2,command = lambda: click_button("-"))
button_equal = Button(root, text = "=", width = 5, height = 2,command = lambda: calculate())

 #add buttons on screen

button_erase.grid(row = 1, column = 0, padx = 5, pady = 5)
button_parenthesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
button_parenthesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
button_div.grid(row = 1, column = 3, padx = 5, pady = 5)

button7.grid(row = 2, column = 0, padx = 5, pady = 5)
button8.grid(row = 2, column = 1, padx = 5, pady = 5)
button9.grid(row = 2, column = 2, padx = 5, pady = 5)
button_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

button4.grid(row = 3, column = 0, padx = 5, pady = 5)
button5.grid(row = 3, column = 1, padx = 5, pady = 5)
button6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
button_subtract.grid(row = 4, column = 3, padx = 5)

button0.grid(row = 5, column = 0,columnspan= 2, padx = 5)
button_point.grid(row = 5, column = 2, padx = 5, pady = 5)
button_equal.grid(row = 5, column = 3, padx = 5, pady = 5)

root.mainloop()