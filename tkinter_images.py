from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("My window")
root.iconbitmap("C:/Users/user/Desktop/college/5th sem/tkinter/home.ico")

my_img1=ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("images/4.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("images/5.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

status=Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_backward

	my_label.grid_forget()
	
	my_label=Label(image=image_list[image_number-1])
	button_forward=Button(root,text=">>",command=lambda: forward(image_number+1))
	button_backward=Button(root,text="<<",command=lambda: backward(image_number-1))

	if image_number==5:
		button_forward=Button(root,text=">>",state=DISABLED)

	my_label.grid(row=0,column=0,columnspan=3)
	button_backward.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)
	#update status bar
	status=Label(root,text="Image "+str(image_number) +" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def backward(image_number):
	global my_label
	global button_forward
	global button_backward
	
	my_label.grid_forget()
	my_label=Label(image=image_list[image_number-1])
	button_forward=Button(root,text=">>",command=lambda: forward(image_number+1))
	button_backward=Button(root,text="<<",command=lambda: backward(image_number-1))


	if image_number==1:
		button_backward=Button(root,text="<<",state=DISABLED)

	my_label.grid(row=0,column=0,columnspan=3)
	button_backward.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)
	#upadte status bar
	status=Label(root,text="Image "+str(image_number) + " of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)



button_backward=Button(root,text="<<",command=backward,state=DISABLED)
button_exit=Button(root,text="EXIT",command=root.quit)
button_forward=Button(root,text=">>",command=lambda: forward(2))


'''button_quit=Button(root,text="Exit!!!",command=root.quit)
button_quit.pack()'''

button_backward.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)


root.mainloop()
