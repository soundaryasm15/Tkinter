from tkinter import *
import math as ma
root=Tk()
root.title("Calculator")
e=Entry(root,width=35,borderwidth=5,bg="#9C51F5",fg="black")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
	#e.delete(0,END)
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first_number=e.get()
	global f_num
	global math
	math="addition"
	f_num=int(first_number)
	e.delete(0,END)

def button_equal():
	second_number=e.get()
	e.delete(0,END)

	if math=="addition":
		e.insert(0,f_num+int(second_number))

	if math=="subtraction":
		e.insert(0,f_num-int(second_number))

	if math=="multiplication":
		e.insert(0,f_num*int(second_number))

	if math=="division":
		e.insert(0,f_num/int(second_number))

	if math=="cube":
		e.insert(0,f_num*f_num*f_num)

	if math=="sqrt":
		e.insert(0,ma.sqrt(f_num))

	if math=="square":
		e.insert(0,f_num*f_num)

def button_subtract():
	first_number=e.get()
	global f_num
	global math
	math="subtraction"
	f_num=int(first_number)
	e.delete(0,END)

def button_multiply():
	first_number=e.get()
	global f_num
	global math
	math="multiplication"
	f_num=int(first_number)
	e.delete(0,END)

def button_divide():
	first_number=e.get()
	global f_num
	global math
	math="division"
	f_num=int(first_number)
	e.delete(0,END)

def button_sqrt():
	first_number=e.get()
	global f_num
	global math
	math="sqrt"
	f_num=int(first_number)
	e.delete(0,END)

def button_square():
	first_number=e.get()
	global f_num
	global math
	math="square"
	f_num=int(first_number)
	e.delete(0,END)

def button_cube():
	first_number=e.get()
	global f_num
	global math
	math="cube"
	f_num=int(first_number)
	e.delete(0,END)


#defining buttons
button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1),activebackground="#EF0C7A")
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2),activebackground="#EF0C7A")
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3),activebackground="#EF0C7A")
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4),activebackground="#EF0C7A")
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5),activebackground="#EF0C7A")
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6),activebackground="#EF0C7A")
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7),activebackground="#EF0C7A")
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8),activebackground="#EF0C7A")
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(8),activebackground="#EF0C7A")
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0),activebackground="#EF0C7A")
button_add=Button(root,text="+",padx=39,pady=20,command=button_add,activebackground="#EF0C7A")
button_clear=Button(root,text="Clear",padx=79,pady=20,command=button_clear,activebackground="#EF0C7A")
button_equal=Button(root,text="=",padx=91,pady=20,command=button_equal,activebackground="#EF0C7A")


button_subtract=Button(root,text="-",padx=41,pady=20,command=button_subtract,activebackground="#EF0C7A")
button_multiply=Button(root,text="*",padx=40,pady=20,command=button_multiply,activebackground="#EF0C7A")
button_divide=Button(root,text="/",padx=41,pady=20,command=button_divide,activebackground="#EF0C7A")

button_sqrt=Button(root,text="√n",padx=37,pady=20,command=button_sqrt,activebackground="#EF0C7A")
button_square=Button(root,text="n²",padx=37,pady=20,command=button_square,activebackground="#EF0C7A")
button_cube=Button(root,text="n³",padx=39,pady=20,command=button_cube,activebackground="#EF0C7A")


#placing buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

button_sqrt.grid(row=7,column=0)
button_square.grid(row=7,column=1)
button_cube.grid(row=7,column=2)

root.mainloop()