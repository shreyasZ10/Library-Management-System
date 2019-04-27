from tkinter import *
from tkinter import ttk 
import random as r 
from datetime import datetime
import tkinter.messagebox
import sqlite3
class User:
	def __init__(self,flag):
		self.flag=flag
		self.flag.title("Bharati Vidyapeeth Library")
		self.flag.geometry("1360x500+0+0")
		self.flag.configure(background='powder blue')

	
		
		
		
		Booktitle=StringVar()
		Author=StringVar()
		name=StringVar()
		

		##################3functions######################
		def exit():
			exit=tkinter.messagebox.askyesno("Bharati Vidyapeeth Library","Confirm if you want to exit")
			if exit>0:
				flag.destroy()
				return 

		def reset():
			
			
			Booktitle.set('')
			Author.set('')
			name.set('')

		def fissue():
			self.lblusername.grid_forget()
			self.txtBooktitle.grid_forget()
			self.lblBooktitle.grid_forget()
			self.lblAuthor.grid_forget()
			self.register_submit.grid_forget()
			self.login_cancel.grid_forget()
			self.txtAuthor.grid_forget()
			self.txtBooktitl.grid_forget()

		def fret():
			self.lbluser.grid_forget()
			self.txtBookhead.grid_forget()
			self.lblBooktitl.grid_forget()
			self.txtBooktit.grid_forget()
			self.registersubmit.grid_forget()
			self.logincancel.grid_forget()

		def issue_book():
			self.lblusername=Label(DataframeLeft,font=('arial',12,'bold'),text="Enter your username",padx=2,pady=2)
			self.lblusername.grid(row=1,column=0,sticky=W)
			self.txtBooktitl=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=name)
			self.txtBooktitl.grid(row=1,column=1)
			self.lblBooktitle=Label(DataframeLeft,font=('arial',12,'bold'),text="Book Title:",padx=2,pady=2)
			self.lblBooktitle.grid(row=2,column=0,sticky=W)
			self.txtBooktitle=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Booktitle)
			self.txtBooktitle.grid(row=2,column=1)
			self.lblAuthor=Label(DataframeLeft,font=('arial',12,'bold'),text="Author:",padx=2,pady=2)
			self.lblAuthor.grid(row=2,column=2,sticky=W)
			self.txtAuthor=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Author)
			self.txtAuthor.grid(row=2,column=3)
			self.register_submit=Button(DataframeLeft,text="Issue",command=issuebook)
			self.register_submit.grid(row=3,column=0)
			self.login_cancel=Button(DataframeLeft,text="cancel",command=fissue)
			self.login_cancel.grid(row=3,column=1)

		def retbook():
			self.lbluser=Label(DataframeLeft,font=('arial',12,'bold'),text="Enter your username",padx=2,pady=2)
			self.lbluser.grid(row=1,column=0,sticky=W)
			self.txtBookhead=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=name)
			self.txtBookhead.grid(row=1,column=1)
			self.lblBooktitl=Label(DataframeLeft,font=('arial',12,'bold'),text="Book Title:",padx=2,pady=2)
			self.lblBooktitl.grid(row=2,column=0,sticky=W)
			self.txtBooktit=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=Booktitle)
			self.txtBooktit.grid(row=2,column=1)
			self.registersubmit=Button(DataframeLeft,text="Return",command=return_book)
			self.registersubmit.grid(row=3,column=0)
			self.logincancel=Button(DataframeLeft,text="cancel",command=fret)
			self.logincancel.grid(row=3,column=1)



		def issuebook():
			title=Booktitle.get()
			author=Author.get()
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			login=cursor.execute('SELECT * from books WHERE title=? AND author=?',(title,author))
			if cursor.fetchall():
				
				check()
			else:
				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Enter Valid details!")

		def check():
			
			name1=name.get()
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			cursor.execute('SELECT * FROM login where username=? and book is null',(name1,))
			if cursor.fetchall():
				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Book Issued !")
				delete()
				addbooktouser()
			else:
				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Return your book first!")

		def delete():
			name1=name.get()
			title=Booktitle.get()
			author=Author.get()
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			cursor.execute('UPDATE books SET quantity = quantity - 1 WHERE title = ?',(title,))
		
			conn.commit()

		def addbooktouser():
			name1=name.get()
			title=Booktitle.get()
			author=Author.get()
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			cursor.execute('UPDATE login SET book = ? WHERE username = ?',(title,name1))
			conn.commit()

		

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
				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "You have no such book!")
					
			
			conn.commit()

		def display():
			conn = sqlite3.connect('Library.db')
			with conn:
				cursor=conn.cursor()
			cursor.execute('SELECT title,author from books')
			rows=cursor.fetchall()
			top = Toplevel()
			top.geometry("400x400")
			top.title("Books")
			

			for index, dat in enumerate(rows):
				self.display=Label(top, text=dat[0]).grid(row=index+1, column=0)
				self.display=Label(top, text=dat[1]).grid(row=index+1, column=1)




			




		
			
			





	

		



























		Mainframe=Frame(self.flag)
		Mainframe.grid()
		TitleFrame=Frame(Mainframe,width=1360,padx=10,bd=20,relief=RIDGE)
		TitleFrame.pack(side=TOP)
		self.lbltitle=Label(TitleFrame,width=39,font=('algerian',40,'bold'),text="\tBharati Vidyapeeth Library\t",padx=12)
		self.lbltitle.grid()
		ButtonFrame=Frame(Mainframe,bd=20,width=1360,height=50,padx=20,relief=RIDGE)
		ButtonFrame.pack(side=BOTTOM)
		
		Dataframe=Frame(Mainframe,bd=20,width=1360,height=400,padx=20,relief=RIDGE)
		Dataframe.pack(side=BOTTOM)
		DataframeLeft=LabelFrame(Dataframe,bd=10,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'))
		DataframeLeft.pack(side=LEFT)
		
	####################################widgets########################################
		
		
		
		

		
		
		

		

	



	#############################################buttons#################################################3
		self.btndisplaydata=Button(ButtonFrame,text='Issue Book',font=('arial',12,'bold'),width=30,bd=4,command=issue_book)
		self.btndisplaydata.grid(row=0,column=0)
		
		self.btnReset=Button(ButtonFrame,text='Display books',font=('arial',12,'bold'),width=30,bd=4,command=display)
		self.btnReset.grid(row=0,column=1)
		self.btnExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width=30,bd=4,command=exit)
		self.btnExit.grid(row=0,column=2)






		




flag=Tk()
application=User(flag)
flag.mainloop()