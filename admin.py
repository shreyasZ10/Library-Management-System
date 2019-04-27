from tkinter import *
from tkinter import ttk 
import random as r 
import tkinter.messagebox
import sqlite3
class Librarian:
	def __init__(self,root):
		self.root=root
		self.root.title("Bharati Vidyapeeth Library")
		self.root.geometry("1360x500+0+0")
		self.root.configure(background='powder blue')

	
		
		
		
		Booktitle=StringVar()
		Author=StringVar()
		Quantity=StringVar()
		name=StringVar()
		

		##################3functions######################
		def fadd():
			self.lblBooktitle.grid_forget()
			self.txtBooktitle.grid_forget()
			self.lblAuthor.grid_forget()
			self.txtAuthor.grid_forget()
			self.lblqty.grid_forget()
			self.register_submit.grid_forget()
			self.txtqty.grid_forget()
			self.cancel.grid_forget()


		def fdel():
			self.lblBooktitle.grid_forget()
			self.txtBooktitle.grid_forget()
			self.lblAuthor.grid_forget()
			self.txtAuthor.grid_forget()
			self.lblqty.grid_forget()
			self.register_submit.grid_forget()
			self.txtqty.grid_forget()
			self.cancel.grid_forget()

		def fret():
			self.lbluser.grid_forget()
			self.txtBookhead.grid_forget()
			self.cancel.grid_forget()
			self.lblBooktitl.grid_forget()
			self.txtBooktit.grid_forget()
			self.registersubmit.grid_forget()


		def reset():
			
			
			Booktitle.set('')
			Author.set('')
			Quantity.set('')


		def fd():
			self.cancel.grid_forget()
			self.display.grid_forget()



		def Addbook():
			title=Booktitle.get()
			author=Author.get()
			quantity=Quantity.get()
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			cursor.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,author TEXT,quantity INTEGER)')
			cursor.execute('INSERT INTO books (title,author,quantity) VALUES(?,?,?)',(title,author,quantity))
			conn.commit()

		def add_book():
			self.lblBooktitle=Label(DataframeLeft,font=('arial',12,'bold'),text="Book Title:",padx=2,pady=2)
			self.lblBooktitle.grid(row=1,column=0,sticky=W)
			self.txtBooktitle=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Booktitle)
			self.txtBooktitle.grid(row=1,column=1)
		
			self.lblAuthor=Label(DataframeLeft,font=('arial',12,'bold'),text="Author:",padx=2,pady=2)
			self.lblAuthor.grid(row=1,column=2,sticky=W)
			self.txtAuthor=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Author)
			self.txtAuthor.grid(row=1,column=3)
			self.lblqty=Label(DataframeLeft,font=('arial',12,'bold'),text="Quantity",padx=2,pady=2)
			self.lblqty.grid(row=1,column=4,sticky=W)
			self.txtqty=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Quantity)
			self.txtqty.grid(row=1,column=5)
			self.register_submit=Button(DataframeLeft,text="Submit",command=Addbook)
			self.register_submit.grid(row=2,column=0)
			self.cancel=Button(DataframeLeft,text="cancel",command=fadd)
			self.cancel.grid(row=2,column=1)


		def delete_book():
			self.lblBooktitle=Label(DataframeLeft,font=('arial',12,'bold'),text="Book Title:",padx=2,pady=2)
			self.lblBooktitle.grid(row=1,column=0,sticky=W)
			self.txtBooktitle=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Booktitle)
			self.txtBooktitle.grid(row=1,column=1)
		
			self.lblAuthor=Label(DataframeLeft,font=('arial',12,'bold'),text="Author:",padx=2,pady=2)
			self.lblAuthor.grid(row=1,column=2,sticky=W)
			self.txtAuthor=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Author)
			self.txtAuthor.grid(row=1,column=3)
			self.lblqty=Label(DataframeLeft,font=('arial',12,'bold'),text="Quantity",padx=2,pady=2)
			self.lblqty.grid(row=1,column=4,sticky=W)
			self.txtqty=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Quantity)
			self.txtqty.grid(row=1,column=5)
			self.register_submit=Button(DataframeLeft,text="Submit",command=Deletebook)
			self.register_submit.grid(row=2,column=0)
			self.cancel=Button(DataframeLeft,text="cancel",command=fdel)
			self.cancel.grid(row=2,column=1)

		def Deletebook():
			title=Booktitle.get()
			author=Author.get()
			quantity=Quantity.get()
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			
			cursor.execute('DELETE FROM books WHERE title=? and author=? and quantity=?',(title,author,quantity))
			conn.commit()

		def retbook():
			self.lbluser=Label(DataframeLeft,font=('arial',12,'bold'),text="Enter username",padx=2,pady=2)
			self.lbluser.grid(row=1,column=0,sticky=W)
			self.txtBookhead=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=name)
			self.txtBookhead.grid(row=1,column=1)
			self.lblBooktitl=Label(DataframeLeft,font=('arial',12,'bold'),text="Book Title:",padx=2,pady=2)
			self.lblBooktitl.grid(row=2,column=0,sticky=W)
			self.txtBooktit=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Booktitle)
			self.txtBooktit.grid(row=2,column=1)
			self.registersubmit=Button(DataframeLeft,text="Return",command=return_book)
			self.registersubmit.grid(row=3,column=0)
			
			self.cancel=Button(DataframeLeft,text="cancel",command=fret)
			self.cancel.grid(row=3,column=1)

		def return_book():
			name1=name.get()
			title=Booktitle.get()
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			cursor.execute('SELECT * FROM login where username=? and book is NOT null',(name1,))
			if cursor.fetchall():
				cursor.execute('UPDATE books SET quantity = quantity + 1 WHERE title = ?',(title,))
				cursor.execute('UPDATE login SET book = null WHERE username = ?',(name1,))
				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Returned book successfully!")
			else:
				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "This user has no such book!")
	
			
			conn.commit()

		def display():
			#self.cancel=Button(DataframeLeft,text="cancel",command=fd)
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			cursor.execute('SELECT name,book from login')
			obj=cursor.fetchall()
			height = len(obj)
			width = height
			top = Toplevel()
			top.geometry("400x400")
			top.title("Users")
			


			for index, dat in enumerate(obj):
				self.display=Label(top, text=dat[0]).grid(row=index+1, column=0)
				self.display=Label(top, text=dat[1]).grid(row=index+1, column=1)
			
			



			
				
		




























	###########################frame##############################
		Mainframe=Frame(self.root)
		Mainframe.grid()
		TitleFrame=Frame(Mainframe,width=1360,padx=10,bd=20,relief=RIDGE)
		TitleFrame.pack(side=TOP)
		self.lbltitle=Label(TitleFrame,width=39,font=('algerian',40,'bold'),text="\tBharati Vidyapeeth Library\t",padx=12)
		self.lbltitle.grid()
		ButtonFrame=Frame(Mainframe,bd=20,width=1360,height=100,padx=20,relief=RIDGE)
		ButtonFrame.pack(side=BOTTOM)
		
		Dataframe=Frame(Mainframe,bd=20,width=1360,height=400,padx=20,relief=RIDGE)
		Dataframe.pack(side=BOTTOM)
		DataframeLeft=LabelFrame(Dataframe,bd=10,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'))
		DataframeLeft.pack(side=LEFT)
		
	####################################widgets########################################
		
		
		
		

		
		
		

		

	



	#############################################buttons#################################################
		self.btndisplaydata=Button(ButtonFrame,text='Add book',font=('arial',12,'bold'),width=30,bd=4,command=add_book)
		self.btndisplaydata.grid(row=0,column=0)
		self.btndisplaydata=Button(ButtonFrame,text='Delete book',font=('arial',12,'bold'),width=30,bd=4,command=delete_book)
		self.btndisplaydata.grid(row=0,column=1)
		self.btnReset=Button(ButtonFrame,text='Return book',font=('arial',12,'bold'),width=30,bd=4,command=retbook)
		self.btnReset.grid(row=0,column=2)
		self.btnExit=Button(ButtonFrame,text='Display Records',font=('arial',12,'bold'),width=30,bd=4,command=display)
		self.btnExit.grid(row=0,column=3)
		






		




root=Tk()
application=Librarian(root)
root.mainloop()