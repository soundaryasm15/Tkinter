from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Database")
root.iconbitmap("C:/Users/user/Desktop/college/5th sem/tkinter/home.ico")
root.geometry("400x600")


#create table
'''c.execute("""CREATE TABLE addresses(
	first_row text,
	last_name text,
	address text,
	city text,
	state text,
	zipcode integer)
	""")'''
#creating a save function
def save():
	conn=sqlite3.connect('address_book.db')
	#create cursor
	c=conn.cursor()#it is to send of the data and get the results
	record_id=delete_box.get()
	c.execute("""UPDATE addresses SET 
		first_row=:first,
		last_name=:last,
		address=:address,
		city=:city,
		state=:state,
		zipcode=:zipcode

		WHERE oid=:oid""",
		{'first':f_name_up.get(),
		 'last':l_name_up.get(),
		 'address':addr_up.get(),
		 'city':city_up.get(),
		 'state':state_up.get(),
		 'zipcode':zcode_up.get(),

		 'oid':record_id
		})

	conn.commit()#commit changes
	conn.close()#close database
	editor.destroy()

#creating an update function
def update():
	global editor
	editor=Tk()
	editor.title("Update a record")
	editor.iconbitmap("C:/Users/user/Desktop/college/5th sem/tkinter/home.ico")
	editor.geometry("400x200")

	conn=sqlite3.connect('address_book.db')
	#create cursor
	c=conn.cursor()#it is to send of the data and get the results

	#query the database
	record_id=delete_box.get()
	c.execute("SELECT * FROM addresses WHERE oid="+record_id)
	records=c.fetchall()#or fetchone() or fetchmany(34=number of records)
	#print(records)
	#creating global variables
	global f_name_up
	global l_name_up
	global addr_up
	global city_up  
	global state_up  
	global zcode_up  
	
	#text boxes
	f_name_up=Entry(editor,width=30)
	f_name_up.grid(row=0,column=1,padx=20,pady=(10,0))#we can create padding only in one side by giving the value as tuple

	l_name_up=Entry(editor,width=30)
	l_name_up.grid(row=1,column=1)

	addr_up=Entry(editor,width=30)
	addr_up.grid(row=2,column=1)

	city_up=Entry(editor,width=30)
	city_up.grid(row=3,column=1)

	state_up=Entry(editor,width=30)
	state_up.grid(row=4,column=1)

	zcode_up=Entry(editor,width=30)
	zcode_up.grid(row=5,column=1)

	

	#text box labels
	f_name_label_up=Label(editor,text="First name")
	f_name_label_up.grid(row=0,column=0,pady=(10,0))

	l_name_label_up=Label(editor,text="Last name")
	l_name_label_up.grid(row=1,column=0)

	addr_label_up=Label(editor,text="Address")
	addr_label_up.grid(row=2,column=0)

	city_label_up=Label(editor,text="City")
	city_label_up.grid(row=3,column=0)

	state_label_up=Label(editor,text="State")
	state_label_up.grid(row=4,column=0)

	zcode_label_up=Label(editor,text="Zipcode")
	zcode_label_up.grid(row=5,column=0)

	#creating a save button to save an edited record
	save_btn=Button(editor,text="Save Record",command=save)
	save_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

	#loop through results
	for record in records:
		f_name_up.insert(0,record[0])
		l_name_up.insert(0,record[1])
		addr_up.insert(0,record[2])
		city_up.insert(0,record[3])
		state_up.insert(0,record[4])
		zcode_up.insert(0,record[5])
	
	# conn.commit()#commit changes
	# conn.close()#close database

# creating a function to delete
def delete():
	conn=sqlite3.connect('address_book.db')
	#create cursor
	c=conn.cursor()#it is to send of the data and get the results

	#delete a record
	c.execute("DELETE FROM addresses WHERE oid= "+delete_box.get())

	conn.commit()#commit changes
	conn.close()#close database



def submit():
	#create a database or connect to one

	conn=sqlite3.connect('address_book.db')
	#create cursor
	c=conn.cursor()#it is to send of the data and get the results

	#insert into table
	c.execute("INSERT INTO addresses values(:f_name,:l_name,:addr,:city,:state,:zcode)",
		{
 			'f_name':f_name.get(),
 			'l_name':l_name.get(),
 			'addr':addr.get(),
 			'city':city.get(),
 			'state':state.get(),
 			'zcode':zcode.get()
 		})
 		
	conn.commit()#commit changes
	conn.close()#close database
	#clear the text box
	f_name.delete(0,END)
	l_name.delete(0,END)
	addr.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zcode.delete(0,END)


def query():
	#create a database or connect to one

	conn=sqlite3.connect('address_book.db')
	#create cursor
	c=conn.cursor()#it is to send of the data and get the results

	#query the database
	c.execute("SELECT *,oid FROM addresses")
	records=c.fetchall()#or fetchone() or fetchmany(34=number of records)
	#print(records)

	#loop through results
	print_records=''
	for record in records:
		print_records+=str(record[0])+" "+str(record[1])+" "+"\t\t"+str(record[6]) +"\n"

	print(print_records)
	query_label=Label(root,text=print_records)
	query_label.grid(row=12,column=0,columnspan=2)

	conn.commit()#commit changes
	conn.close()#close database

#text boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))#we can create padding only in one side by giving the value as tuple

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

addr=Entry(root,width=30)
addr.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=4,column=1)

zcode=Entry(root,width=30)
zcode.grid(row=5,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=10)



#text box labels
f_name_label=Label(root,text="First name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last name")
l_name_label.grid(row=1,column=0)

addr_label=Label(root,text="Address")
addr_label.grid(row=2,column=0)

city_label=Label(root,text="City")
city_label.grid(row=3,column=0)

state_label=Label(root,text="State")
state_label.grid(row=4,column=0)

zcode_label=Label(root,text="Zipcode")
zcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="Enter an id: ")
delete_box_label.grid(row=9,column=0,pady=10)

#create submit button
submit_btn=Button(root,text="Add record to database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=111)


#create a query button
query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#create a delete button
delete_btn=Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#create an update button
update_btn=Button(root,text="Update Record",command=update)
update_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=137)


root.mainloop()
