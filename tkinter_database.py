from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Database")
root.iconbitmap("C:/Users/user/Desktop/college/5th sem/tkinter/home.ico")
root.geometry("400x400")


#create table
'''c.execute("""CREATE TABLE addresses(
	first_row text,
	last_name text,
	address text,
	city text,
	state text,
	zipcode integer)
	""")'''
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
		print_records+=str(record[0])+" "+str(record[2])+"\n"
	print(print_records)
	query_label=Label(root,text=print_records)
	query_label.grid(row=8,column=0,columnspan=2)

	conn.commit()#commit changes
	conn.close()#close database

#text boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

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

#text box labels
f_name_label=Label(root,text="First name")
f_name_label.grid(row=0,column=0)

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

#create submit button
submit_btn=Button(root,text="Add record to database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


#create a query button
query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=100)



root.mainloop()
