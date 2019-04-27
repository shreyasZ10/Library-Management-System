from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import sqlite3
import random as r 
from datetime import datetime





class Login:
	def __init__(self,root):
		self.root=root
		self.root.title("Bharati Vidyapeeth Library")
		self.root.geometry("1360x750+0+0")
		self.root.configure(background='powder blue')

		login_user=StringVar()
		login_pwd=StringVar()
		register_name=StringVar()
		register_user=StringVar()
		register_pwd=StringVar()
		admin_user=StringVar()
		admin_pwd=StringVar()

		def database():
   			name1=register_name.get()
   			username=register_user.get()
   			password=register_pwd.get()
   			conn = sqlite3.connect('Library.db')
   			with conn:
   				cursor=conn.cursor()
   			cursor.execute('CREATE TABLE IF NOT EXISTS login(name TEXT,username TEXT,password TEXT,book varchar )')
   			cursor.execute('INSERT INTO login (name,username,password) VALUES(?,?,?)',(name1,username,password))
   			conn.commit()
   			tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Details saved successfully!")
   		
		def exit():
			exit=tkinter.messagebox.askyesno("Bharati Vidyapeeth Library","Confirm if you want to exit")
			if exit>0:
				root.destroy()
				return 

		

		def flogin():
			self.user.grid_forget()
			self.loguser.grid_forget()
			self.pwd.grid_forget()
			self.logpwd.grid_forget()
			self.login_submit.grid_forget()
			self.login_cancel.grid_forget()

		def fadmin():
			self.user.grid_forget()
			self.adminuser.grid_forget()
			self.pwd.grid_forget()
			self.adminpwd.grid_forget()
			self.admin_submit.grid_forget()
			self.login_cancel.grid_forget()

		def fregister():
			self.name.grid_forget()
			self.register_name.grid_forget()
			self.user.grid_forget()
			self.registeruser.grid_forget()
			self.pwd.grid_forget()
			self.registerpwd.grid_forget()
			self.register_submit.grid_forget()
			self.login_cancel.grid_forget()


		def User_login():
			self.user=Label(DataframeLeft,font=('arial',12,'bold'),text="Username",padx=2,pady=2)
			self.user.grid(row=0,column=0,sticky=W)
			self.loguser=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=login_user)
			self.loguser.grid(row=0,column=1)
			self.pwd=Label(DataframeLeft,font=('arial',12,'bold'),text="Password",padx=2,pady=2)
			self.pwd.grid(row=1,column=0,sticky=W)
			self.logpwd=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=login_pwd,show="*")
			self.logpwd.grid(row=1,column=1)
			self.login_submit=Button(DataframeLeft,text="Submit",command=query)
			self.login_submit.grid(row=2,column=0)
			self.login_cancel=Button(DataframeLeft,text="cancel",command=flogin)
			self.login_cancel.grid(row=2,column=1)
			

		def Admin_login():
			self.user=Label(DataframeLeft,font=('arial',12,'bold'),text="Username",padx=2,pady=2)
			self.user.grid(row=0,column=0,sticky=W)
			self.adminuser=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=admin_user)
			self.adminuser.grid(row=0,column=1)
			self.pwd=Label(DataframeLeft,font=('arial',12,'bold'),text="Password",padx=2,pady=2)
			self.pwd.grid(row=1,column=0,sticky=W)
			self.adminpwd=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=admin_pwd,show="*")
			self.adminpwd.grid(row=1,column=1)
			self.admin_submit=Button(DataframeLeft,text="Submit",command=adminquery)
			self.admin_submit.grid(row=2,column=0)
			self.login_cancel=Button(DataframeLeft,text="cancel",command=fadmin)
			self.login_cancel.grid(row=2,column=1)

		def Register():
			self.name=Label(DataframeLeft,font=('arial',12,'bold'),text="Name",padx=2,pady=2)
			self.name.grid(row=0,column=0,sticky=W)
			self.register_name=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=register_name)
			self.register_name.grid(row=0,column=1)
			self.user=Label(DataframeLeft,font=('arial',12,'bold'),text="Username",padx=2,pady=2)
			self.user.grid(row=2,column=0,sticky=W)
			self.registeruser=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=register_user)
			self.registeruser.grid(row=2,column=1)
			self.pwd=Label(DataframeLeft,font=('arial',12,'bold'),text="Password",padx=2,pady=2)
			self.pwd.grid(row=3,column=0,sticky=W)
			self.registerpwd=Entry(DataframeLeft,font=('arial',12,'bold'),width=25,textvariable=register_pwd,show="*")
			self.registerpwd.grid(row=3,column=1)
			self.register_submit=Button(DataframeLeft,text="Submit",command=database)
			self.register_submit.grid(row=4,column=0)

			self.login_cancel=Button(DataframeLeft,text="cancel",command=fregister)
			self.login_cancel.grid(row=4,column=1)

		def query():
   			username=login_user.get()
   			password=login_pwd.get()
   			conn=sqlite3.connect('Library.db')
   			with conn:
   				cursor=conn.cursor()
   			login=cursor.execute('SELECT * from login WHERE username=? AND password=?',(username,password))
   			if cursor.fetchall():
   				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Welcome User!")
   				root.destroy()
   				import user
   				
   				
   				
   			else:
   				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Enter valid details!")
		def adminquery():
   			username=admin_user.get()
   			password=admin_pwd.get()
   			conn=sqlite3.connect('library.db')
   			with conn:
   				cursor=conn.cursor()
   			login=cursor.execute('SELECT * from admin WHERE username=? AND password=?',(username,password))
   			if cursor.fetchall():
   				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Welcome Admin!")
   				root.destroy()
   				import admin

   			else:
   				tkinter.messagebox.showinfo("Bharati Vidyapeeth Library", "Not an Admin!")

		


		




		Mainframe=Frame(self.root)
		Mainframe.grid()
		TitleFrame=Frame(Mainframe,width=1360,padx=10,bd=20,relief=SUNKEN)
		TitleFrame.pack(side=TOP)
		self.lbltitle=Label(TitleFrame,width=39,font=('algerian',40,'bold'),text="\tBharati Vidyapeeth Library\t",padx=12)
		self.lbltitle.grid()
		ButtonFrame=Frame(Mainframe,bd=20,width=1360,height=50,padx=20,relief=RIDGE)
		ButtonFrame.pack(side=BOTTOM)

		Dataframe=Frame(Mainframe,bd=20,width=1360,height=400,padx=20,relief=RIDGE)
		Dataframe.pack(side=BOTTOM)
		DataframeLeft=LabelFrame(Dataframe,bd=10,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'))
		DataframeLeft.pack(side=LEFT)
		
		self.admin=Button(ButtonFrame,text='Admin',font=('arial',12,'bold'),width=30,bd=4,command=Admin_login)
		self.admin.grid(row=0,column=0)
		self.login=Button(ButtonFrame,text='Login',font=('arial',12,'bold'),width=30,bd=4,command=User_login)
		self.login.grid(row=0,column=1)
		self.register=Button(ButtonFrame,text='Register',font=('arial',12,'bold'),width=30,bd=4,command=Register)
		self.register.grid(row=0,column=2)
		self.reset=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width=30,bd=4,command=exit)
		self.reset.grid(row=0,column=3)

		
		


		
	





root=Tk()
application=Login(root)
root.mainloop()

