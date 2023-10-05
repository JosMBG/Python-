from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql

#Base de datos------------------------------------------------------------------
#Clase Poo, funciones------------------------------------------------------------------




class DataBase:
	def __init__(self):

		self.connection = pymysql.connect(
			host='localhost', 
			user='root',
			password='',
			db='Base_Curso'
		)

		self.cursor = self.connection.cursor()
		print("conexion establecida")
	
	def read(self):
		ide=idC.get()
		#print(ide)
		sql = 'SELECT id, name, email,edad FROM user WHERE id = {}'.format(ide)
		try:
			self.cursor.execute(sql)
			user = self.cursor.fetchone()

			print("Id:", user[0]) 
			print("name:", user[1])
			nameP.set(user[1])
			print("Email:", user [2])
			emailP.set(user[2])
			print("Edad:", user [3])
			edadP.set(user[3])

		except Exception as e:
			raise
	
	def mensaje(self):
		pass

	def update(self):
		ide=idC.get()
		uname=nombreC.get()
		uedad=edadC.get()
		uemail=emailC.get()
		

		sql="UPDATE user SET email='{}', name='{}', edad={} WHERE id={}".format(uemail,uname,uedad,ide)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
			info2.config(fg="green", text="Datos actualizados")

		except Exception as e:
			raise

	def delete(self):
		ide=idC.get()

		sql="DELETE FROM user WHERE id={}".format(ide)

		try:
			self.cursor.execute(sql)
			self.connection.commit()
			info2.config(fg="red", text="Datos borrados")
			

		except Exception as e:
			raise

	def insert(self):
		uname=nombreC.get()
		uedad=edadC.get()
		uemail=emailC.get()

		sql = "INSERT INTO user (name,edad,email) VALUES ('{}',{},'{}')".format(uname,uedad,uemail)

		try:
			self.cursor.execute(sql)
			self.connection.commit()
			info2.config(fg="blue", text="Datos agregados")
			

		except Exception as e:
			raise


	def close(self):
		self.connection.close()
		root.destroy()

	def clean(self):
		nameP.set("")
		edadP.set("")
		emailP.set("")
		idP.set("")





database = DataBase()


root = tk.Tk()
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='db.png'))
root.title("Gestor DB")
miFrame = Frame(width=300, height=400)
root.geometry("300x250")
miFrame.pack()
#Datos------------------------------------------------------------------
#ID------------------------------------------------------------------
id=Label(miFrame, text="ID: ")
id.grid(row=0,column=0)

idP=StringVar()
idC=Entry(miFrame, textvariable=idP)
idC.grid(row=0,column=1)
#Nombre------------------------------------------------------------------
nombre=Label(miFrame, text="Nombre:")
nombre.grid(row=1,column=0)

nameP=StringVar()
nombreC=Entry(miFrame, textvariable=nameP)
nombreC.grid(row=1,column=1)
#edad------------------------------------------------------------------
edad=Label(miFrame, text="Edad:")
edad.grid(row=2, column=0)

edadP=StringVar()
edadC=Entry(miFrame, textvariable=edadP)
edadC.grid(row=2, column=1)
#Email------------------------------------------------------------------
email=Label(miFrame, text="Email:")
email.grid(row=3,column=0)

emailP=StringVar()
emailC=Entry(miFrame,textvariable=emailP)
emailC.grid(row=3, column=1)
#Botones-------------------------------------------------------------------
miFrame2=Frame(root)
miFrame2.pack()

Create=Button(miFrame2, text="Create", width=3, command=lambda:database.insert())
Create.grid(row=4,column=0)

Update=Button(miFrame2, text="Update", width=3,command=lambda:database.update())
Update.grid(row=4,column=1)

Read=Button(miFrame2, text="Read", width=3, command=lambda:database.read())
Read.grid(row=4,column=2)

Delete=Button(miFrame2, text="Delete", width=3, command=lambda:database.delete())
Delete.grid(row=4,column=3)

#info------------------------------------------------------------------
info=Label(miFrame2, text="->Para read introduce la id")
info.grid(row=5,column=0, columnspan=4)

info=Label(miFrame2, text="->Para Create introduce nombre,edad, email")
info.grid(row=6,column=0, columnspan=4)

info=Label(miFrame2, text="->Para Delete introduce la id")
info.grid(row=7,column=0, columnspan=4)

info=Label(miFrame2, text="->Para Update introduce todo")
info.grid(row=8,column=0, columnspan=4)

info=Label(miFrame2, text="SOLO INTRODUCIR CAMPOS NECESARIOS")
info.grid(row=9,column=0, columnspan=4)

info2=Label(miFrame2, text="Status")
info2.grid(row=10,column=0, columnspan=4)

#database.close()

#menu-----------------------------------------------------------------------
Bmenu=Menu(root)
root.config(menu=Bmenu)
Bmenu.config(bg="grey")

opciones=Menu(Bmenu, tearoff=0)
opciones.add_command(label="Salir", command=lambda:database.close())
opciones.add_command(label="Limpiar", command=lambda:database.clean())


ayuda=Menu(Bmenu, tearoff=0)



Bmenu.add_cascade(label="Opciones", menu=opciones)
Bmenu.add_cascade(label="Ayuda", menu=ayuda)


miFrame.mainloop()


