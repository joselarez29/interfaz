import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Usuario():
	def __init__(self):         
		self.user = ' '         
		self.nombre = ' '         
		self.cedula= ' '
		self.rif= ' '
		self.contraseña= ' '
		self.tipocli= ' '
		self.direccion= ' '
		self.telefono= ' '
		
lista=list()
			
def cliente():
	def mensaje():
		messagebox.showinfo('Anuncio','Guardado satisfactoriamente, enviaremos el pedido a su direccion, nos comunicaremos por telefono')
		
	vcliente=tk.Tk()
	vcliente.title("Python TRUZZBLOGG GUI")
	vcliente.geometry("500x300")
	vcliente.resizable(False,False)
	vcliente.config(width=300, height=200)
	vcliente.title('Pedir Comida')
	Label(vcliente, text="Ingrese la cantidad en unidades").place(x=125, y=20)
	Label(vcliente, text="Pizza 5$").place(x=90, y=40)
	Label(vcliente, text="Hamburguesa 3$").place(x=90, y=70)
	Label(vcliente, text="Perro Caliente 1$").place(x=90, y=100)
	Label(vcliente, text="Shawarma 3$").place(x=90, y=130)
	Label(vcliente, text="Refresco 0.5$").place(x=90, y=160)
	Button(vcliente, text="Ingresar registro", command=mensaje).place(x=200, y=200)
	# Crear caja de texto.
	pizz = ttk.Entry(vcliente)
	hamb= ttk.Entry(vcliente)
	perroc= ttk.Entry(vcliente)
	shawa= ttk.Entry(vcliente)
	refre= ttk.Entry(vcliente)
	
	# Posicionarla en la ventana.
	pizz.place(x=200, y=40)
	hamb.place(x=200, y=70)
	perroc.place(x=200, y=100)
	shawa.place(x=200, y=130)
	refre.place(x=200, y=160)
	vcliente.mainloop()
			
def funcion():
	segunda=tk.Tk()
	segunda.title("Python TRUZZBLOGG GUI")
	segunda.geometry("500x300")
	segunda.resizable(False,False)
	segunda.config(width=300, height=200)
	segunda.title('Registrarse')
	Label(segunda, text="Usuario").place(x=90, y=20)
	Label(segunda, text="Contraseña").place(x=90, y=40)
	Label(segunda, text="Cedula").place(x=90, y=60)
	Label(segunda, text="Rif").place(x=90, y=80)
	Label(segunda, text="Nombre").place(x=90, y=100)
	Label(segunda, text="Cliente ó Proveedor").place(x=90, y=120)
	Label(segunda, text="Direccion").place(x=90, y=140)
	Label(segunda, text="Telefono").place(x=90, y=160)
	Button(segunda, text="Registrarse", command=cliente).place(x=200, y=200)
	
	# Crear caja de texto.
	usu = ttk.Entry(segunda)
	contra= ttk.Entry(segunda)
	cedu= ttk.Entry(segunda)
	rif= ttk.Entry(segunda)
	nom= ttk.Entry(segunda)
	clipro= ttk.Entry(segunda)
	dire= ttk.Entry(segunda)
	tel= ttk.Entry(segunda)
	
	# Posicionarla en la ventana.
	usu.place(x=200, y=20)
	contra.place(x=200, y=40)
	cedu.place(x=200, y=60)
	rif.place(x=200, y=80)
	nom.place(x=200, y=100)
	clipro.place(x=200, y=120)
	dire.place(x=200, y=140)
	tel.place(x=200, y=160)
	def registro():
		H= Usuario()
		H.user=usu
		H.contraseña= contra
		H.cedula=cedu
		H.rif= rif
		H.Nombre= nom
		H.tipocli= clipro
		H.direccion= dire
		H.telefono= tel
		lista.append(H)
	registro()	
	segunda.mainloop()

		
mywindow=tk.Tk()
mywindow.title("Python TRUZZBLOGG GUI")
mywindow.geometry("500x300")
mywindow.resizable(False,False)
mywindow.config(width=300, height=200)
mywindow.title('Envios a Domicilio')
Button(mywindow, text="Iniciar Sesion", command=cliente).place(x=150, y=200)
Button(mywindow, text="Registrarse", command=funcion).place(x=270, y=200)
Label(mywindow, text="Usuario").place(x=90, y=100)
Label(mywindow, text="Contraseña").place(x=90, y=150) 
# Crear caja de texto.
usu = ttk.Entry(mywindow)
contra= ttk.Entry(mywindow)
# Posicionarla en la ventana.
usu.place(x=180, y=100)
contra.place(x=180, y=150)
mywindow.mainloop()
